from django.shortcuts import render
from Product.models import Product
from django.core.paginator import Paginator
from django.db.models import Q



def homedata(request):
    shopdata=Product.objects.all().order_by('-id')[0:]
    top=Product.objects.all().order_by('-id')[0:2]

    search=request.GET.get('getdata')
    if search:
        shopdata=shopdata.filter(
            Q(price__icontains=search)|Q(title__icontains=search)|Q(description__icontains=search)|Q(shop__icontains=search)
        ) 

    paginator = Paginator(shopdata, 9)
    page= request.GET.get('page')
    total_member= paginator.get_page(page)
    context={
        'sp':total_member,
        'last':top,
        
    }
    return render(request,'index.html',context)

