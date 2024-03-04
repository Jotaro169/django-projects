"""
URL configuration for carRental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('home/',home,name='home'),
    path('logout/',logout, name='logout'),

    #adding urls

    path('about/', about, name='about'),
    path('about.html/', about),
    path('booking/',booking, name='booking'),
    path('booking.html/', booking),
    path('service/',service, name='service'),
    path('service.html/', service),
    path('contact/',contact, name='contact'),
    path('contact.html/', contact),
    path('detail/', detail, name='detail'),
    path('detail.html/', detail),
    path('car/', car, name='car'),
    path('car.html/', car),

]
