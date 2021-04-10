from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='userprofile')
    first_name=models.CharField(max_length=100, blank=True)
    last_name=models.CharField(max_length=100, blank=True)
    phone=models.CharField(max_length=100, blank=True)
    email=models.EmailField(max_length=300,blank=True, null=True)
    gender=models.CharField(blank=True,max_length=20)
    address=models.CharField(max_length=500,blank=True)
    image=models.ImageField(upload_to='customer_image/')

    def __str__(self):
        return self.user.first_name
    


