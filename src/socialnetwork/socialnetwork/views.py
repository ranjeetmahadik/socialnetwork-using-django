from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


@login_required(login_url="/accounts/login")
def home(request):
    return render(request,"homes.html",{})

@login_required(login_url="/accounts/login")
def logoutview(request):
    logout(request)
    return redirect("home")
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password == password2:
                form.save()
                user = authenticate(username=username,password=password)
                login(request,user)
            return redirect('home')
    else:
            form = UserCreationForm()
    context = {"form":form}
    return render(request,"registration/register.html",context)
