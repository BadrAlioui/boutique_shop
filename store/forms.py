from django import forms
from .models import Product, Review, Refund


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['reason']
