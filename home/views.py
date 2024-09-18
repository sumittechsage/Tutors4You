from django.shortcuts import render, redirect
# Create your views here.

def IndexPageView(request):
    return render(request, 'index.html') # render index.html

def AboutUsView(request):
    return render(request, 'about_us.html') # render index.html
