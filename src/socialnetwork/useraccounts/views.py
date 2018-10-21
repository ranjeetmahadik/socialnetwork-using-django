from django.views.generic import DetailView
from django.views import View
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .models import UserProfile
User=get_user_model()

class UserDetailView(DetailView):
    template_name = "auth/userdetail.html"
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User,username__iexact=self.kwargs.get('username'))
    def get_context_data(self,*args,**kwargs):
        context = super(UserDetailView,self).get_context_data(*args,**kwargs)
        print(self.kwargs)
        context['following'] = UserProfile.objects.is_following(self.request.user,self.get_object())
        return context

class UserFollow(View):
	def get(self,request,username,*args,**kwargs):
		follow_user = get_object_or_404(User,username__icontains=username)
		if request.user.is_authenticated:
			is_following = UserProfile.objects.to_follow(request.user,follow_user)
		return redirect("profiles:detail",username=username)
