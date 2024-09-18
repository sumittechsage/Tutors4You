from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPageView, name = 'index'),
    path('about-us/', AboutUsView, name = 'about-us'),
]