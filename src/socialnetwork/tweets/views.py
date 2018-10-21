from django.db.models import Q
from django.shortcuts import render
from .models import Tweet
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse_lazy
from django.forms.utils import ErrorList
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .forms import TweetModelForm
from .mixins import UserRequiredMixin
# Create your views here
class TweetDeleteView(LoginRequiredMixin,DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:list")
    template_name = "tweets/delete_confirm.html"

class TweetCreateView(LoginRequiredMixin,UserRequiredMixin,CreateView):
    form_class = TweetModelForm
    template_name = "tweets/createview.html"
    #success_url = reverse_lazy("tweet:detail")
    login_url = "/accounts/login"
    #def form_valid(self,form):
    #    print(self.request.user.is_authenticated)
    #    if self.request.user.is_authenticated:
    #        print(self.request.user)
    #        form.instance.user = self.request.user
    #        return super(TweetCreateView,self).form_valid(form)
    #    else:
    #        form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
    #        return self.form_invalid(form)

def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid() and request.user.is_authenticated():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {"form":form}
    return render(request,"tweets/createview.html",context)

class TweetListView(LoginRequiredMixin,ListView):
    #template_name = "tweet/tweetlist.html"
    queryset = Tweet.objects.all()
    login_url = "/accounts/login"
    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("search",None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query)|
            Q(user__username__icontains=query))
        return qs
    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form'] = TweetModelForm()
        context['action_url'] = reverse_lazy("tweet:create")
        return context

class TweetDetailView(LoginRequiredMixin,DetailView):
    #template_name = "tweet/tweetdetail.html"
    #queryset = Tweet.objects.all()
    login_url = "/accounts/login"
    def get_object(self):
        print(self.kwargs)
        id = self.kwargs['pk']
        return Tweet.objects.get(id=id)

def tweetlist(request):
    qs = Tweet.objects.all()
    context = {"object_list":qs}
    print(context)
    return render(request,"tweets/tweetlist.html",context)


def tweetdetail(request,id=None):
    qs = Tweet.objects.get(id=id)
    context = {"object":qs}
    return render(request,"tweets/tweetdetail.html",context)
