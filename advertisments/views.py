from django.views.generic import ListView, DetailView, CreateView

from .models import Ad
from .forms import AdsCreateForm
from .filters import AdsFilter


class AdsListView(ListView):
    model = Ad
    context_object_name = 'ads_list'
    template_name = 'ads_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads_total'] = Ad.objects.count()
        return context

class AdsDetailView(DetailView):
    model = Ad
    context_object_name = 'ad'
    template_name = 'ads_detail.html'

class AdsCreateView(CreateView):
    model = Ad
    form_class = AdsCreateForm
    template_name = 'ads_create.html'
    redirect_field_name = 'redirect_to'
    context_object_name = 'create_form'

class AdsSearchView(ListView):
    model = Ad
    template_name = 'ads_search.html'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['filter'] = AdsFilter(self.request.GET, queryset=self.get_queryset())
        return context
