from django.shortcuts import render,HttpResponseRedirect, redirect
from .forms import UserLoginForm,UserRegisterForm
from account.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
from .decorators import login_required
from django.conf import settings


def login(request):

    if request.user.is_authenticated:
        return redirect('app:index')

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        remember_me = request.POST.get('remember_me', False)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']  
            password = login_form.cleaned_data['password']
            user_obj = auth.authenticate(request, email=email, password=password)

            if user_obj is not None:
                if remember_me:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                    return redirect('/')
                else:
                    request.session.set_expiry(0)
                    messages.warning(request,'Your session has been expired')
                
                auth.login(request, user_obj)
                messages.success(request, "Login successful!")
                return redirect('app:index')
            else:
                messages.warning(request, "Invalid email or password.")
        else:
            print(login_form.errors)
            messages.warning(request, "Invalid form data. Please try again.")
    
    else:
        login_form = UserLoginForm()

    return render(request, "account/login.html", {'user_login_form': login_form})


def register(request):
    user_register_form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user= True
            user.save()
            user_obj = auth.authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            auth.login(request, user_obj)
            messages.success(request,"Account created successfully !")
            return redirect('app:index')
        else:
            print(form.errors)
            error_messages = [str(error) for error in form.errors.values()]
            for message in error_messages:
                messages.warning(request, message)    
    return render(request,'account/register.html',{'user_register_form':user_register_form})


@login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('app:index')


@login_required
def userprofile(request):
    return render(request,'account/profile.html')


def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request,"Account Deleted Successfully !")
    return redirect('app:profile')


@login_required
def change_password_view(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm = request.POST.get('new_password2')

        if new_password != confirm:
            messages.warning(request,"New password and confirm password not match.")
        
            if request.user.change_password(old_password, new_password):
                messages.success(request, 'Password changed successfully.')
            
            return redirect('account:profile')

        else:
            messages.error(request, 'Invalid old password. Please try again.')

        return redirect('account:profile')  
    else:
        return redirect('account:profile')  
