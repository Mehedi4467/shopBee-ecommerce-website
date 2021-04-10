from django.urls import path
from .import views

urlpatterns = [
    path('',views.shop_Profile, name='shop'),
    path('Upload/',views.upload_product, name='pupload'),
]
