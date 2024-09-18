from django.shortcuts import render, redirect
# Create your views here.

def LoginView(request):
    if request.method == 'POST':
        print("###################")
    return render(request, 'login.html') # render index.html

def RegisterView(request):
    return render(request, 'register.html') # render index.html
