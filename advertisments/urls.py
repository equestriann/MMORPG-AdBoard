from .views import *
from django.urls import path

urlpatterns = [
    path('', AdsListView.as_view(), name='ads_list'),
    path('<int:pk>/', AdsDetailView.as_view(), name='ads_detail'),
    path('create/', AdsCreateView.as_view(), name='ads_create'),
    path('search/', AdsSearchView.as_view(), name='ads_search'),
    path('update/<int:pk>/', AdsUpdateView.as_view(), name='ads_update'),
    path('delete/<int:pk>/', AdsDeleteView.as_view(), name='ads_delete'),
    path('reply/<int:pk>', ReplyCreateView.as_view(), name='reply_create'),
    path('reply/<int:pk>/update', ReplyUpdateView.as_view(), name='reply_update'),
    path('reply/<int:pk>/detail', ReplyDetailView.as_view(), name='reply_detail'),
    path('reply/<int:pk>/delete', ReplyDeleteView.as_view(), name='reply_delete'),
    path('reply/<int:pk>/accept', reply_accept, name='reply_accept'),
    path('my_profile/', UserProfile.as_view(), name='user_profile'),
    path('test', send_mail_test, name='test')
    # path('myprofile', UserAds.as_view(), name='user_profile'),
    # path('my_profile', UserReplies.as_view(), name='user_profile'),
    # path('my_profile', UserAdsReplies.as_view(), name='user_ads_profile'),
]
