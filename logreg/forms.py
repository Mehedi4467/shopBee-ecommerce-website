from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from Profile.models import Customer


class Customer_reg_form(UserCreationForm):
    email=forms.EmailField(max_length=50)


    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']





class user_updateFrom(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']


class userProfile_UpdateForm(forms.ModelForm):
    STATES = (
    ('', 'Choose...'),
    ('Male', 'Male'),
    ('Female', 'Female')
)
    gender=forms.ChoiceField(choices=STATES)
    image=forms.ImageField()
    class Meta:
        model=Customer
        fields= ['phone', 'gender','address','image']