from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Ad, Reply
from .forms import AdsCreateForm, ReplyCreateForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_ad = context.get('ad')
        context['replies_to_this_ad'] = current_ad.replies_to_ad.count()
        return context


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
    paginate_by = 5

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


# -----------------------------------

class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = 'reply_create.html'
    context_object_name = 'create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_title'] = 'Тут должен быть заголовок текущего объявления...'
        return context
