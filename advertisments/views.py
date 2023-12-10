from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Ad
from .forms import AdsCreateForm
from .filters import AdsFilter


class AdsListView(ListView):
    model = Ad
    context_object_name = 'ads_list'
    template_name = 'ads_list.html'
    paginate_by = 5

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
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['filter'] = AdsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class AdsUpdateView(UpdateView):
    template_name = 'ads_create.html'
    form_class = AdsCreateForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get('pk')
        return Ad.objects.get(pk=id_)

class AdsDeleteView(DeleteView):
    template_name = 'ads_delete.html'
    success_url = '/'
    queryset = Ad.objects.all()
