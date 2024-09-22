import os
from django.contrib import messages
from django.shortcuts import render, redirect

from home.models import UserQuery
# Create your views here.


def IndexPageView(request):
    try:
        email = os.getenv('EMAIL_HOST_USER')
        phone_no = os.getenv('PHONE_NUMBER')
        return render(request, 'index.html', {'email' : email, 'phone_no' : phone_no}) # render index.html
    except Exception as e:  
        print("exception in index view: ", str(e))


def UserQueryView(request):
    try:
        data = request.POST
        query = UserQuery(
            email = data['email'],
            phone_no = data['phone_no'],
            name = data['name'],
            message = data['message']
        )
        query.save()
        messages.success(request, 'Query Submitted')
        return redirect('index') 
    
    except Exception as e:
        print("exception in query view: ", str(e))
        messages.error(request, 'Something Went Wrong')
        return redirect('index') 
