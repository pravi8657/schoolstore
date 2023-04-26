from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.mail import message
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import bio


# Create your views here.

def new(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        cp = request.POST['cpassword']
        if p == cp:
            if User.objects.filter(username=u).exists():
                messages.info(request, 'username already taken')
                return redirect('reg')

        user = User.objects.create_user(username=u, password=p)
        user.save()
        messages.info(request,'succesfully registered')
        return redirect('reg')
    return render(request,'reglogin.html')

def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=u,password=p)
        if user is not None:
            auth.login(request,user)
            return redirect('bio')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def detail(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        DOB = request.POST.get('DOB', )
        Age = request.POST.get('Age', )
        Gender = request.POST.get('Gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        department = request.POST.get('department', )
        material = request.POST.get('material', )
        bio1 = bio(name=name, DOB=DOB, Age=Age, Gender=Gender, phone=phone, email=email, address=address,
                   department=department, material=material)
        bio1.save()

        messages.info(request, 'successfully submitted')
    return render(request, 'bio.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request,'form.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
