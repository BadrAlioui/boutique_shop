from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('product/<product_id>/update/', views.update_product, name='update_product'),
    path('product/<product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/<product_id>/', views.product_detail, name='product_detail'),
]


