import os
from django.shortcuts import render, redirect
# Create your views here.


def IndexPageView(request):
    return render(request, 'index.html') # render index.html

def AboutUsView(request):
    email = os.getenv('EMAIL_HOST_USER')
    phone_no = os.getenv('PHONE_NUMBER')
    return render(request, 'about_us.html', {'email' : email, 'phone_no' : phone_no}) # render index.html
