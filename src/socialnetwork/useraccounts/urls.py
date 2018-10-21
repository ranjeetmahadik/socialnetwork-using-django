from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import UserDetailView,UserFollow
urlpatterns = [
    #url(r'^$', RedirectView.as_view(url="/")),
    #url(r'^search/$', TweetListView.as_view(),name="list"),
    url(r'^(?P<username>[\w.@+-]+)/$',UserDetailView.as_view(),name="detail"),
    url(r'^(?P<username>[\w.@+-]+)/follow/$',UserFollow.as_view(),name="follow"),
    #url(r'^create/$', TweetCreateView.as_view(),name="create"),
    #url(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(),name="delete"),
]
