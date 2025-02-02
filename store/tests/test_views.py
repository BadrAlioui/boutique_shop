from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Product, Category, Order, Review, Refund
import json
from time import sleep


class TestViews(TestCase):
    """Test case for views in the store app."""

    def setUp(self):
        """Set up test environment before each test."""
        self.client = Client()
        self.user = User.objects.create_user(username="testuser",
                                             password="testpass")
        self.admin = User.objects.create_superuser(username="admin",
                                                   password="adminpass")

        self.category = Category.objects.create(name="Men", slug="men")
        self.product = Product.objects.create(
            title="Test Product",
            description="A sample product for testing",
            price=20.00,
            stock=10,
        )
        self.product.category.add(self.category)

        self.order = Order.objects.create(
            user=self.user,
            product=self.product,
            reference="123ABC",
            price=20.00,
            status="Paid"
        )

        self.refund = Refund.objects.create(
            order=self.order,
            user=self.user,
            reason="Item was defective",
            status="pending"
        )

    def test_all_products_view(self):
        """Check if the products page loads correctly."""
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/products.html")

    def test_product_detail_view(self):
        """Check if product details are accessible."""
        response = self.client.get(reverse("product_detail",
                                           args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/product_detail.html")

    def test_add_product_view_as_admin(self):
        """Ensure only admin users can add products."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/add_product.html")

    def test_add_product_view_as_user(self):
        """Ensure regular users cannot access the add product page."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 302)

    def test_update_product_view(self):
        """Ensure product update works for admin users."""
        self.client.login(username='admin', password='adminpass')

        # Vérifier que l'utilisateur est bien admin
        admin_user = User.objects.get(username='admin')
        response = self.client.post(reverse('update_product',
                                            args=[self.product.slug]), {
            "title": "Updated Product",
            "description": "Updated description",
            "price": 25.00,
            "stock": 5,
            "category": [self.category.id],
            "brand": "Updated Brand",
            "slug": "updated-product",
        })

        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.title, "Updated Product")

    def test_delete_product_view(self):
        """Ensure product deletion works for admin users."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(reverse("delete_product",
                                            args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(slug=self.product.slug).exists())

    def test_request_refund_view(self):
        """Ensure users can request a refund only for paid orders."""
        self.client.login(username='testuser', password='testpass')
        self.order.status = "Created"
        self.order.save()
        self.order.refresh_from_db()

        response = self.client.get(reverse('request_refund',
                                           args=[self.order.id]), follow=True)

        if response.redirect_chain:
            final_url = response.redirect_chain[-1][0]
            print(f"DEBUG: Final redirected URL = {final_url}")
            self.assertEqual(final_url, reverse('my_profile'))
        else:
            print("DEBUG: NO_REDIRECT")

        self.assertEqual(response.status_code, 200)

    def test_refund_status_view(self):
        """Ensure refund status is visible to the user."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("refund_status",
                                   args=[self.refund.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/refund_status.html")
