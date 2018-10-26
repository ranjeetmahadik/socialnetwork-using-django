from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import registerview
from django.contrib.auth.views import login,logout
urlpatterns = [
    url(r'^login/$', login,{"template_name":"accounts/login.html"}),
    url(r'^logout/$', logout,{"template_name":"accounts/logout.html"}),
    url(r'^register/$', registerview,name="register"),

]
