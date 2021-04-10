from django.shortcuts import render,redirect
from Profile.models import Customer
from django.contrib.auth.models import User
from logreg.forms import user_updateFrom,userProfile_UpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse



@login_required(login_url='/Logreg/login') 
def customer_P(request):
    current_user=request.user
    accountData=Customer.objects.get(user_id=current_user.id)
    context={
        'Ad':accountData,
        
    }
  
    return render(request, 'customerprofile.html',context)





def shopProfile(request):
    return HttpResponse("This is a shopkeeper Profile")




@login_required(login_url='/Logreg/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = user_updateFrom(request.POST, instance=request.user)
        profile_form = userProfile_UpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('Cprofile')
    else:
        user_form = user_updateFrom(instance=request.user)
        profile_form = userProfile_UpdateForm(instance=request.user)
        
        context = {
          
            'user_form': user_form,
            'profile_form': profile_form,
           
        }
        return render(request, 'update_user.html', context)



@login_required(login_url='/Logreg/login')
def user_password_update(request):
    if request.method == "POST":
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Your Password has been updated!')
            return redirect('Cprofile')
        else:
            messages.success(request, 'Please correct the error Below!.')
            return redirect('pass')

    else:
      form=PasswordChangeForm(request.user) 
      return render(request, 'pass.html',{'form':form})