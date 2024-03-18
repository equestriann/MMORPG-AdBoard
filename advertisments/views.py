from pprint import pprint

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse

from django.shortcuts import redirect

from .models import Ad, Reply
from .forms import AdsCreateForm, ReplyCreateForm
from .filters import AdsFilter

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator

from django.contrib import messages

from .tasks import send_test_email


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

    def form_valid(self, form):
        ad = form.save(commit=False)
        form.instance.author = self.request.user
        ad.save()
        return super().form_valid(form)


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
    success_url = '/my_profile'
    queryset = Ad.objects.all()


# -----------------------------------

class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = 'reply_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.get(pk=self.kwargs['pk'])
        # pprint(context)
        return context

    def form_valid(self, form):
        reply = form.save(commit=False)
        form.instance.author = self.request.user
        reply.ad = Ad.objects.get(pk=self.kwargs['pk'])
        reply.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reply_detail', kwargs={'pk': self.object.pk})


class ReplyUpdateView(LoginRequiredMixin, UpdateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = 'reply_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pprint(context)
        context['ad'] = Reply.objects.get(pk=self.kwargs['pk']).ad
        # pprint(context)
        return context

    def get_success_url(self):
        return reverse('reply_detail', kwargs={'pk': self.object.pk})


class ReplyDetailView(LoginRequiredMixin, DetailView):
    model = Reply
    context_object_name = 'reply'
    template_name = 'reply_detail.html'
    login_url = 'login'


class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'reply_delete.html'
    success_url = '/my_profile'
    queryset = Reply.objects.all()


def reply_accept(request, pk):
    reply = Reply.objects.get(pk=pk)

    if not reply.is_accepted:
        reply.accept()
    else:
        reply.reject()

    return redirect(request.META.get('HTTP_REFERER'), pk)


# -----------------------------------
class UserProfile(ListView):
    template_name = "profile_scroll.html"
    model = Ad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = Ad.objects.filter(author=self.request.user)
        context['replies'] = Reply.objects.filter(author=self.request.user).all()
        context['replies_to_self_ads'] = Reply.objects.filter(ad__author=self.request.user).all()

        return context


def send_mail_test(request):
    send_test_email.delay(request.user.id)

    return redirect('user_profile')
