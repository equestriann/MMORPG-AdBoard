from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Ad
from .forms import AdsCreateForm


class AdsListView(ListView):
    model = Ad
    context_object_name = 'ads_list'
    template_name = 'templates/ads_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads_total'] = Ad.objects.count()
        # pprint(context)
        return context

class AdsDetailView(DetailView):
    model = Ad
    context_object_name = 'ad'
    template_name = 'templates/ads_detail.html'

class AdsCreateView(CreateView):
    model = Ad
    form_class = AdsCreateForm
    template_name = 'templates/ads_create.html'
    redirect_field_name = 'redirect_to'
    context_object_name = 'create_form'