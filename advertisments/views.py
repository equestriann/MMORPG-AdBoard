from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse

from .models import Ad, Reply
from .forms import AdsCreateForm, ReplyCreateForm
from .filters import AdsFilter

from django.contrib.auth.mixins import LoginRequiredMixin


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


class AdsCreateView(LoginRequiredMixin, CreateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filter'] = AdsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class AdsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'ads_create.html'
    form_class = AdsCreateForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get('pk')
        return Ad.objects.get(pk=id_)


class AdsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'ads_delete.html'
    success_url = '/'
    queryset = Ad.objects.all()


# -----------------------------------

class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = 'reply_create.html'
    context_object_name = 'reply'

    def form_valid(self, form):
        reply = form.save(commit=False)
        ad = Ad.objects.get(pk=self.kwargs['pk'])
        reply.ad = ad
        reply.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_title'] = Ad.objects.get(pk=self.kwargs['pk']).title
        return context

    def get_success_url(self):
        return reverse('reply_detail', kwargs={'pk': self.object.pk})


class ReplyDetailView(LoginRequiredMixin, DetailView):
    model = Reply
    context_object_name = 'reply'
    template_name = 'reply_user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_reply = Reply.objects.get(pk=self.kwargs['pk'])
        context['reply_date'] = current_reply.date_sent
        context['reply_text'] = current_reply.text
        is_accepted = current_reply.is_accepted

        if is_accepted is True:
            context['is_accepted'] = 'Отклик принят'
        else:
            context['is_accepted'] = 'В ожидании'

        return context


# -----------------------------------
class UserProfile(ListView):
    template_name = "user_profile.html"
    model = Ad

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = Ad.objects.filter(author=self.request.user).all()
        context['replies'] = Reply.objects.filter(author=self.request.user).all()
        return context
