from .views import *
from django.urls import path

urlpatterns = [
    path('register/', user_register, name='register_url'),
    path('success/', login_success, name='login_success'),
    path('logout/', user_logout, name='logout_url'),
    path('logout_success', logout_success, name='logout_success'),
    path('login', user_login, name='login_process'),
]
