from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .models import *
from django.http import HttpResponse


# Create your views here.

def home(request):
    car = Car.objects.all()
    cust_id =request.session.get('cust_id')
    return render(request, 'index.html', {'cars': car, 'cust_id': cust_id})


def login(request):
    try:
        if request.method == 'POST':
            uname = request.POST.get('username')
            pass1 = request.POST.get('pass')
            cust_obj = Customer.objects.get(email=uname)
            if cust_obj.email == uname:
                if cust_obj.password == pass1:
                    request.session['cust_id'] = cust_obj.cust_id
                    request.session['cust_email'] = cust_obj.email
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'msg': "Email or password incorrect", "uname": uname, "pass1": pass1})
    except Customer.DoesNotExist:
        return render(request, 'login.html', {'msg': "Customer does not exist", "uname": uname, "pass1": pass1})
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        phone = request.POST.get('phone')
        dl_no = request.POST.get('dl')
        add = request.POST.get('address')
        dl_image = request.FILES.get('dl_image')
        cust_image = request.FILES.get('cust_image')
        new_cust = Customer(name=uname, email=email, password=pass1, is_verified=0, phone_no=phone, dl_no=dl_no, address=add, dl_image=dl_image, cust_image=cust_image)
        new_cust.save()
        print('user created')
        return redirect('login')
    return render(request, 'signup.html')


def logout(request):
    user_logout(request)
    return redirect('home')
