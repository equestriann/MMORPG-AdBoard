from .views import *
from django.urls import path

urlpatterns = [
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login', user_login, name='login'),
    path('activate', activate_account, name='account_activation')
]
