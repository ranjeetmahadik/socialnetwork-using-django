from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import tweetlist,tweetdetail,TweetListView,TweetDeleteView,TweetDetailView,TweetCreateView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(),name="list"),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name="detail"),
    url(r'^create/$', TweetCreateView.as_view(),name="create"),
    url(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(),name="delete"),
]
