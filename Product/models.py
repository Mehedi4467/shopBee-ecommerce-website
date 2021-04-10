from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    shop=models.CharField(max_length=200, blank=False)
    title=models.CharField(max_length=300, blank=False)
    img=models.ImageField(blank=True, upload_to='product/')
    price=models.CharField(blank=False,max_length=200)
    band=models.CharField(blank=True,max_length=200)
    description=models.TextField(max_length=1000, blank=True)


    def __str__(self):
        return self.shop + ' ==>' + self.title



class Invoice(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    fname=models.CharField(blank=True,max_length=200)
    lname=models.CharField(blank=True,max_length=200)
    shop=models.CharField(max_length=200, blank=True)
    title=models.CharField(max_length=300, blank=False)
    img=models.ImageField(blank=True, upload_to='product/')
    price=models.CharField(blank=False,max_length=200)
    band=models.CharField(blank=True,max_length=200)
    description=models.TextField(max_length=1000, blank=True)
    address=models.CharField(blank=False,max_length=300)
    city=models.CharField(blank=False,max_length=300)
    division=models.CharField(blank=False,max_length=300)
    phone=models.EmailField(blank=False,max_length=300)
    method=models.CharField(max_length=20,blank=False)
    send_number=models.CharField(blank=False,max_length=15)
    txid=models.CharField(blank=False,max_length=300)

    


