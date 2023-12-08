from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ad


class AdsListView(ListView):
    model = Ad
    context_object_name = 'ads_list'
    template_name = 'templates/ads_list.html'

class AdsDetailView(DetailView):
    model = Ad
    context_object_name = 'ad'
    template_name = 'templates/ads_detail.html'