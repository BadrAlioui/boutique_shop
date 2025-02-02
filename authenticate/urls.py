from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('password/', views.change_password, name='change_password'),
    path('profile/', views.my_profile, name='my_profile'),
]
