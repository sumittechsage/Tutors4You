from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView, name = 'login'),
    path('register/', RegisterView, name = 'register'),
]