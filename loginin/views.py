from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.auth.models import User

# Create your views here.

def loginin(request):
    if request.user.is_authenticated:
        context= {'user':request.user}
        print(request.user.profile.role)
        print(request.user.username)
        # print(User.objects.get(username="mitraaji").profile)
        # print(request.user.role)
        return render (request, 'halamanLogin.html',context)
    else:
        return render(request,"halamanLogin.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.role = form.cleaned_data.get('role')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
