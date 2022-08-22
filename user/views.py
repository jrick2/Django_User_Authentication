from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import  User
from django.contrib import messages
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "user/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "user/login.html", {
                "message": "Invalid Credentials"
            })

    return render(request, "user/login.html")

def logout_view(request):
    logout(request)
    return render(request, "user/login.html")

def sign_up(request):
    if request.method == "POST":
        email = request.POST['email']
        user = request.POST['user']
        password1 = request.POST['pass1']
        password2 =  request.POST['pass2']

        if password1 != password2:
            messages.info(request,'Passworn do not match')
            return redirect("sign_up")
            if User.objects.filter(username=user).exists():
                messages.info(request,'Username Already exist')
                return redirect("sign_up")

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already exist')
                return redirect("sign_up")
            else:
                user = User.objects.create_user(email=email,username=user,password=password1)
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

        else:
            messages.info(request, "Passsword do not match")
            return HttpResponseRedirect(reverse("sign_up"))
        
    return render(request, "user/sign-up.html")
