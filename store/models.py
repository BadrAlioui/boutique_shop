from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, default="default-slug")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True, default="default-slug")
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.1)])
    image = CloudinaryField('images', null = True, blank=True)
    stock = models.IntegerField(default=0, blank=True, verbose_name="Stock du produit")

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.title


    @property
    def in_stock(self) -> bool:
        return self.stock > 0

    
    def clean(self):
        if self.stock < 0:
            raise ValidationError("Stock cannot be negative")
        if self.price < 0:
            raise ValidationError("Price cannot be negative")

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.title}"

    @property
    def average_rating(self):
        reviews = Review.objects.filter(product=self.product)
        if reviews.exists():
            return round(reviews.aggregate(models.Avg('rating'))['rating__avg'], 1)
        return "No ratings yet"


    def clean(self):
        if self.rating is None:
            raise ValidationError("Rating cannot be empty.")

        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5.")



class Order(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    reference = models.CharField(max_length=128)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, default="Created")
    price = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        user_str = self.user.username if self.user else "Unknown User"
        product_str = self.product.title if self.product else "Unknown Product"
        return f"Order by {user_str} for {product_str} ({self.get_size_display()}) - Status: {self.status}"


class Refund(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="refunds")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Refund request for Order {self.order.id} - {self.status.capitalize()}"