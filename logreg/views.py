from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate,login
from .forms import Customer_reg_form
from django.contrib.auth.models import User
from Profile.models import Customer
from django.contrib import messages

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "User Name or Passwod Incarret")
    return render(request,'login.html')



def reg(request):
    form = Customer_reg_form(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            current_user = request.user
            data = Customer()
            data.user_id = current_user.id
            data.image = "customer_image/user.png"
            data.save()
            return redirect('home')
        else:
             messages.warning(request, "Password And re Password does not mach")
    context={
        'form':form
    }
    return render(request,'reg.html',context)





def customer_logout(request):
    logout(request)
    return redirect('home')
