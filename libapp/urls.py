from django.contrib import admin
from django.urls import path,include
from libapp import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home,name='home'),
    path('user_logout/',views.user_logout),
    path('update_profile/',views.update_profile),
    path('getbook/',views.getbook),
    path('about/',views.about),
    path('contactus/',views.contactus),
] 