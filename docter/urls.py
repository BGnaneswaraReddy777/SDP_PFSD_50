from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',DocterHomepage,name='DocterHomepage'),
    path('DocterLogin/',DocterLogin,name='DocterLogin'),
    path('Docterlogin1/',Docterlogin1,name='Docterlogin1'),
    path('DocterSignup/',DocterSignup,name='DocterSignup'),
    path('Doctersignup1/',Doctersignup1,name='Doctersignup1'),
    path('Docterlogout/',Docterlogout,name='Docterlogout'),
    path('DocterConsultation/',DocterConsultation,name='DocterConsultation'),
]
