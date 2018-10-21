from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tweets.views import TweetListView
from .views import register,home,logoutview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^register/', register,name="register"),
    url(r'^$', TweetListView.as_view(),name="home"),
    url(r'^logout/$',logoutview,name="logout"),
    url(r'^tweets/',include(('tweets.urls','tweet'),namespace='tweet')),
    url(r'^api/tweet/',include(('tweets.api.urls','tweet-api'),namespace='tweet-api')),
    url(r'^',include(('useraccounts.urls','profiles'),namespace='profiles')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
