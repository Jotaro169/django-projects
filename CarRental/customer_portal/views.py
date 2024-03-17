from django.shortcuts import render, redirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .models import *
from django.http import HttpResponse
from .models import Customer
import re  # Import regular expression module
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
import string

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
        email = request.POST.get('email')
        try:
            cust_obj = Customer.objects.get(email=email)
            if cust_obj.email == email:
                return render(request, 'signup.html', {'msg': "Email already exist"})
        except:
            pass
        uname = request.POST.get('username')
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


# adding code for forgot password
# def changePassword(request):
#     return render(request,'change-password.html')



#     except Exception as e:
#         print(e)
#     return render(request,'forget-password.html')


def logout(request):
    user_logout(request)
    return redirect('home')

def cars(request):
    car = Car.objects.all()
    cust_id = request.session.get('cust_id')
    return render(request, 'cars.html', {'cars': car, 'cust_id': cust_id})


def carDetails(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    cust_id = request.session.get('cust_id')
    return render(request, 'carDetails.html', {'cars': [car], 'cust_id': cust_id})

def booking(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    cust_id = request.session.get('cust_id')
    return render(request,'booking.html', {'cars': [car], 'cust_id': cust_id})

def profile(request):
    cust_id =request.session.get('cust_id')
    cust_obj = Customer.objects.get(cust_id=cust_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        uname = request.POST.get('username')
        phone = request.POST.get('phone')
        dl_no = request.POST.get('dl')
        add = request.POST.get('address')
        dl_image = request.FILES.get('dl_image')
        cust_image = request.FILES.get('cust_image')
        pass1 = cust_obj.password
        if cust_image == None or cust_image == '':
            cust_image = cust_obj.cust_image
        if dl_image == None or dl_image == '':
            dl_image = cust_obj.dl_image
        if email == None or email == '':
            email = cust_obj.email
        new_cust = Customer(cust_id=cust_id ,name=uname, email=email, phone_no=phone,password=pass1, dl_no=dl_no, address=add, dl_image=dl_image, cust_image=cust_image)
        new_cust.save()
        cust_obj = Customer.objects.get(cust_id=cust_id)
    return render(request, 'profile.html', {'cust': cust_obj, 'cust_id': cust_id})



def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            cust_obj = Customer.objects.get(email=email)
            if cust_obj.cust_id == 0:
                return render(request, 'forgotPassword.html',{'msg': 'Please enter correct email, user not found with given email address'})
        except:
            pass

        email = request.POST['email']
        all_characters = string.ascii_letters + string.digits
        password = ''.join(random.choices(all_characters, k=10))
        message = """Hello from car castle,  
        Your new generated password is: """ + password

        cust_obj = Customer.objects.get(email=email)
        cust_obj.password = password
        cust_obj.save()
        send_mail('Contact Form', message, 'settings.EMAIL_HOST_USER',
                  [email], fail_silently = False)
        return render(request, 'forgotPassword.html',{'msg': 'We have sent you email to change password'})
    return render(request ,'forgotPassword.html')

