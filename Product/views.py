from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from Product.models import Product,Invoice
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

def productdata(request):
    pdata=Product.objects.all().order_by('-id')[0:]

    search=request.GET.get('dataget')
    if search:
        pdata=pdata.filter(
            Q(price__icontains=search)|Q(title__icontains=search)|Q(description__icontains=search)|Q(shop__icontains=search)
        ) 

    paginator = Paginator(pdata, 9)
    page= request.GET.get('page')
    total_member= paginator.get_page(page)

    context={
        'p':pdata
    }
    return render(request,'product.html',context)


def checkoutdata(request,id):
    cheekout=get_object_or_404(Product, pk=id)
    context={
        'c':cheekout
    }
    return render(request, 'cheekout.html',context)


def invoicearea(request,id):
    alldata=get_object_or_404(Product, pk=id)
    context={
        'all':alldata
    }
    return render(request, 'invoice.html',context)


@login_required(login_url='/Logreg/login') 
def busproduct(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        shop=request.POST.get('shop')
        title=request.POST.get('title')
        img=request.FILES.get('img')
        price=request.POST.get('price')
        band=request.POST.get('band')
        description=request.POST.get('description')
        address=request.POST.get('address')
        city=request.POST.get('city')
        division=request.POST.get('division')
        phone=request.POST.get('phone')
        method=request.POST.get('method')
        send_number=request.POST.get('send_number')
        txid=request.POST.get('txid')

        
        current_user = request.user
        alldata=Invoice(fname=fname,lname=lname,address=address,division=division,city=city,method=method,send_number=send_number,txid=txid,shop=shop, title=title, img=img, price=price, band=band, description=description,phone=phone)
        alldata.user_id = current_user.id
        
        if txid:
        
            alldata.save()
            return redirect('bmyuy')
        else:
            return redirect('by')
    return render(request,'index.html')



def myBuy(request):
    allbuy=Invoice.objects.filter(user=request.user).order_by('-id')[0:]
    context={
        'buy':allbuy
    }
    return render(request, 'mybuy.html', context)