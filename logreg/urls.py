from django.urls import path
from .import views

urlpatterns = [
    path('login',views.customer_login, name='log'),
    path('Registation',views.reg, name='reg'),
    path('logout',views.customer_logout, name='logout'),
    
]
