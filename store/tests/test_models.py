from django.core.exceptions import ValidationError
from store.models import Category, Product, Order, Refund
from django.test import TestCase
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.category = Category.objects.create(name='test category')
        self.product = Product.objects.create(
            title='test product',
            description='test description',
            price=10.00,
            stock=10
        )
        self.product.category.add(self.category)

        self.order = Order.objects.create(
            user=self.user,
            product=self.product,
            reference='test reference',
            price=10.00
        )

    def test_in_stock(self):
        self.assertTrue(self.product.in_stock)
        self.product.stock = 0
        self.assertFalse(self.product.in_stock)
        self.product.stock = -1
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_category_model(self):
        self.assertEqual(str(self.category), 'test category')

    def test_product_model(self):
        self.assertEqual(str(self.product), 'test product')
        self.assertTrue(self.product.in_stock)
        self.product.stock = 0
        self.assertFalse(self.product.in_stock)
        self.product.stock = -1
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_order_model(self):
        self.assertIn(f"Order by {self.user.username} for {self.product.title}", str(self.order))
        self.assertIn("Status: Created", str(self.order))

    def test_refund_model(self):
        refund = Refund.objects.create(
            order=self.order,
            user=self.user,
            reason="Test refund reason",
            status="pending"
        )
        self.assertEqual(str(refund), f"Refund request for Order {self.order.id} - Pending")



