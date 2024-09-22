from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPageView, name = 'index'),
    path('query/', UserQueryView, name = 'user-query'),
]