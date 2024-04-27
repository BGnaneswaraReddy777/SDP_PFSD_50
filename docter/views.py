from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import string
import random
# Create your views here.
from .models import Docter
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

import string
import random
def DocterHomepage(request):
    return render(request, 'Docterhomepage.html')
def DocterConsultation(request):
    return render(request, 'Docterconsultationpage.html')
def DocterLogin(request):
    return render(request,'DocterLogin.html')
def DocterSignup(request):
    return render(request,'Doctersignup.html')


def Docterlogin1(request):
    if request.method == 'POST':
        Docusername = request.POST.get('Docusername')
        Docterpassword = request.POST.get('Docterpassword')
        try:
            docter = Docter.objects.get(Docusername=Docusername, Docterpassword=Docterpassword)
        except Docter.DoesNotExist:
            return render(request, 'DocterLogin.html', {'error_message': 'Invalid credentials'})

        # Add the docter object to the context
        return render(request, 'Docterhomepage.html', {'Docter': docter})
    else:
        messages.info(request, 'Verification unsuccesfull!')
        # Render the login page for GET request
        return render(request, 'DocterLogin.html')



def Doctersignup1(request):
    if request.method == "POST":
        Docusername = request.POST['Docusername']
        Docterpassword = request.POST['Docterpassword']
        Docterpassword1 = request.POST['Docterpassword1']
        Docteremail = request.POST['Docteremail']  # Get email from POST data
        # phone = request.POST['phone'] # Get phone number from POST data
        googlelink=request.POST['googlelink']
        doc= Docter(Docusername=Docusername, Docterpassword=Docterpassword,Docteremail =Docteremail, googlelink=googlelink)
        doc.save()
        messages.info(request, 'Verifying')
        a=input()
        b="verified"
        if(a==b):
            messages.info(request, 'Verification succesfull!')
            return render(request, 'DocterLogin.html')
        else:
            messages.info(request, 'Verification unsuccesfull!')
            return render(request, 'Doctersignup.html')
from django.contrib.auth import logout

from django.contrib.auth import logout

def Docterlogout(request):
    logout(request)
    return render(request, 'Docterhomepage.html')
