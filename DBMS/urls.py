
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Home.urls")),
    path('Profile/',include("Profile.urls")),
    path('Product/',include("Product.urls")),
    path('Logreg/',include("logreg.urls")),
    path('Shop/',include("Myshop.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
