from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from Myshop.forms import Upload_productFrom
from Product.models import Product
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url='/Logreg/login') 
def shop_Profile(request):
    shopdata=Product.objects.filter(user=request.user).order_by('-id')[0:]
    context={
        'sp':shopdata
    }
    return render(request, 'shop.html',context)






@login_required(login_url='/Logreg/login') 
def upload_product(request):
    if request.method == 'POST':
        shop=request.POST.get('shop')
        title=request.POST.get('title')
        img=request.FILES.get('img')
        price=request.POST.get('price')
        band=request.POST.get('band')
        description=request.POST.get('description')
        current_user = request.user
        alldata=Product(shop=shop, title=title, img=img, price=price, band=band, description=description)
        alldata.user_id = current_user.id
        
        if img:
        
            alldata.save()
            return redirect('shop')
        else:
            return redirect('upload')
    return render(request,'upload.html')