from .views import *
from django.urls import path

urlpatterns = [
    path('register/', user_register, name='register_url'),
    path('success/', user_login, name='login_success'),
    path('logout/', user_logout, name='logout_url'),
    path('login', user_login, name='login_process'),
]
