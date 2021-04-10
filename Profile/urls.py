from django.urls import path
from .import views

urlpatterns = [
    path('customer_profile/',views.customer_P, name='Cprofile'),
    path('shop_profile/',views.shopProfile, name='shop'),
    path('User_upadate/',views.user_update, name='update'),
    path('User_password/',views.user_password_update, name='pass'),
]
