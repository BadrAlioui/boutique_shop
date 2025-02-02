from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('product/<slug:slug>/update/', views.update_product,
         name='update_product'),
    path('product/<slug:slug>/delete/', views.delete_product,
         name='delete_product'),
    path('product/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('<str:slug>/process_payment/', views.process_payment,
         name='process_payment'),
    path('<str:reference>/success/', views.payment_success, name='success'),
    path('<str:reference>/cancel/', views.payment_cancel, name='cancel'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('refunds/request/<int:order_id>/', views.request_refund,
         name='request_refund'),
    path('refunds/status/<int:refund_id>/',
         views.refund_status, name='refund_status'),
]
