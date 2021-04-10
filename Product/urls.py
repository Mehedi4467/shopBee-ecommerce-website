from django.urls import path
from .import views


urlpatterns = [
    path('Products/',views.productdata, name='product'),
    path('Checkout/<int:id>',views.checkoutdata, name='check'),
    path('Invoice/<int:id>',views.invoicearea, name='in'),
    path('busproduct/',views.busproduct, name='by'),
    path('My_Purchase/',views.myBuy, name='bmyuy'),
]
 



