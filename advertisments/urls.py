from .views import *
from django.urls import path

urlpatterns = [
    path('', AdsListView.as_view(), name = 'ads_list'),
    path('<int:pk>', AdsDetailView.as_view(), name = 'ads_detail'),
]