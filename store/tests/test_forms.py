from django.test import TestCase
from store.forms import ProductForm, ReviewForm, RefundForm
from store.models import Category, Product, Review, Order, Refund
from django.contrib.auth.models import User

class TestForms(TestCase):

    def setUp(self):
        """Set up test objects for the forms."""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            title="Test Product",
            description="Test description",
            price=10.00,
            stock=5,
        )
        self.order = Order.objects.create(
            user=self.user,
            product=self.product,
            reference='123ABC',
            price=10.00,
            status='Paid'
        )

    def test_valid_product_form(self):
        """Ensure a valid product form is accepted."""
        form = ProductForm(data={
            'title': 'New Product',
            'description': 'A great product',
            'price': 20.00,
            'stock': 10,
            'category': [self.category.id],
            'brand': 'Test Brand',
            'slug': 'new-product',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_product_form(self):
        """Ensure an invalid product form is rejected."""
        form = ProductForm(data={
            'title': '',  # Missing title
            'description': 'A product',
            'price': -5,  # Negative price
            'stock': -10  # Negative stock
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)  # Ensure title error exists
        self.assertIn('price', form.errors)  # Ensure price error exists
        self.assertIn('__all__', form.errors)  # Ensure overall form validation error
        self.assertIn('Stock cannot be negative', str(form.errors['__all__']))  

    def test_valid_review_form(self):
        """Ensure a valid review form is accepted."""
        form = ReviewForm(data={
            'rating': 5,
            'comment': 'Great product!'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_review_form(self):
        """Ensure a review form with an invalid rating is rejected."""
        form = ReviewForm(data={
            'rating': None,  # Missing rating
            'comment': 'Good'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)  # Ensure rating error exists

    def test_valid_refund_form(self):
        """Ensure a valid refund request form is accepted."""
        form = RefundForm(data={
            'reason': 'Item arrived damaged'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_refund_form(self):
        """Ensure an empty refund request form is rejected."""
        form = RefundForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('reason', form.errors)  # Ensure reason error exists
