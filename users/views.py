from django.shortcuts import render, redirect
from django.contrib import messages
from users.decorators import unauthenticated_user
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import Profile
# Create your views here.

@unauthenticated_user
def registerform(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            myuser = form.save()
            p = Profile(user=myuser)
            p.first_name = myuser.first_name
            p.last_name = myuser.last_name
            p.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created {username}, you can now login!')
            return redirect('login')
        else:
            messages.error(request, form.errors)
            return redirect('register')
    else:
        form = UserRegisterForm()
            
            
    return render(request, 'users/register.html', {'form': form})


@unauthenticated_user
def loginform(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog-home')
        else:
            messages.info(request, f'Username Or Password is incorrect')
                
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userprofile(request):

    return render(request, 'users/userprofile.html')


@login_required(login_url='login')
def userupdate(request):
    if request.method == 'POST':
        profileupdateform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if profileupdateform.is_valid():
            profileupdateform.save()
            messages.success(request, f'Your profile has been successfully updated!')
            return redirect('userprofile')
        else:
            messages.warning(request, profileupdateform.errors)
            return redirect('userupdate')
    else: 
        profileupdateform = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'profileupdateform': profileupdateform
    }

    return render(request, 'users/userupdate.html', context)
