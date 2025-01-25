from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from .models import Product, Category, Order
from .forms import ProductForm
from django.contrib.auth.decorators import user_passes_test, login_required
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Lower
import stripe
import uuid
import json

# Configuration de la clé Stripe
stripe.api_key = "votre_clé_secrète"  


def admin_required(user):
    return user.is_superuser


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    query = None
    sort = None
    direction = None
    selected_category = None

    if request.GET:
        # Gestion du tri
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Gestion de la recherche
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # Gestion du filtre par catégorie
        if 'category' in request.GET:
            selected_category = request.GET['category']
            products = products.filter(category__slug=selected_category)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'store/products.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)


@user_passes_test(admin_required)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'store/add_product.html'
    context = {'form': form}
    return render(request, template, context)


@user_passes_test(lambda user: user.is_superuser)
def update_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)

    template = 'store/update_product.html'
    context = {'form': form, 'product': product}
    return render(request, template, context)


@user_passes_test(lambda user: user.is_superuser)
def delete_product(request, slug):
    """Vue pour supprimer un produit"""
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect(reverse('products'))

    template = 'store/delete_product.html'
    context = {'product': product}
    return render(request, template, context)


def payment_success(request, reference):
    """Vue pour afficher le succès du paiement"""
    product_slug = request.session.get('product')
    product = get_object_or_404(Product, slug=product_slug)
    order_reference = request.session.get('order')
    order = get_object_or_404(Order, reference=order_reference)

    order.status = "Paid"
    order.save()

    del request.session['product']
    del request.session['order']

    messages.success(request, "Payment successful!")
    return redirect('product_detail', product_id=product.id)


def payment_cancel(request, reference):
    """Vue pour afficher l'annulation du paiement"""
    order_reference = request.session.get('order')
    order = get_object_or_404(Order, reference=order_reference)
    order.status = "Cancelled"
    order.save()

    request.session.pop('order')
    messages.error(request, "Payment cancelled!")
    return redirect('products')


@login_required(login_url='/accounts/login/')
def process_payment(request, slug):
    """Vue pour traiter le paiement avec Stripe"""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    product = get_object_or_404(Product, slug=slug)
    user = request.user

    if request.method == "POST":
        size = request.POST.get('size')  # Récupère la taille choisie depuis le formulaire

        if size not in ['S', 'M', 'L', 'XL']:
            messages.error(request, "Invalid size selected.")
            return redirect('product_detail', product_id=product.id)

        pre_transaction = uuid.uuid4().hex[:6]

        order = Order(
            user=user,
            product=product,
            size=size,  # Ajout de la taille à la commande
            reference=pre_transaction,
            date=datetime.now(),
            status="Created",
            price=product.price,
        )
        order.save()

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=user.email,
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': int(product.price * 100),
                        'product_data': {
                            'name': f"{product.title} ({size})",  # Ajout de la taille au titre
                            'description': product.description,
                            'images': [request.build_absolute_uri(product.image.url)] if product.image else [],
                        },
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            metadata={
                'order_id': order.reference,
            },
            success_url=request.build_absolute_uri(reverse('success', args=[pre_transaction])),
            cancel_url=request.build_absolute_uri(reverse('cancel', args=[pre_transaction])),
        )

        request.session['product'] = product.slug
        request.session['order'] = order.reference

        return redirect(session.url)

    return render(request, 'store/product_detail.html', {'product': product})



@csrf_exempt
def stripe_webhook(request):
    """Webhook Stripe pour mettre à jour le statut des commandes"""
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError:
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session.get('metadata')['order_id']
        try:
            order = Order.objects.get(reference=order_id)
        except Order.DoesNotExist:
            return HttpResponse(status=404)
        order.status = "Paid"
        order.save()

    return HttpResponse(status=200)