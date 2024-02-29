from .views import *
from django.urls import path

urlpatterns = [
    path('register/', user_register, name='register_url'),
]
