from . models import User
from django import forms
from django.contrib.auth.hashers import make_password
import re

''' user login form '''
class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    phone_no = forms.CharField(widget=forms.NumberInput())
    class Meta:
        model  = User
        fields =['name','email','phone_no','password','confirm_password']
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        phone_No = cleaned_data.get('phone_no')

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match!")
        
        if len(password) < 8:
            raise forms.ValidationError("Password contain at least 8 character long.")
        
        # if not re.match(r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}|:";<>,.?`~]).*$', password):
        #     raise forms.ValidationError("Password must contain at least one number, one uppercase letter, and one special character.")


        if not re.match(r'^[0-9]{10}$', phone_No):
            raise forms.ValidationError("Enter a valid phone number.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user