from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.models import User #Import the User module
from django.contrib.auth import authenticate,login,logout#import some more stuff
from .models import *
# /
def start(request):
    form = forms.SignUp()
    
    return render(request,"Mesmerise/index.html",{"form":form})

#signAction    
def SignAction(request):
    if request.method == 'POST':

        form = forms.SignUp(request.POST,request.FILES)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print("works")

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email=form.cleaned_data["email"]
            
            bio=form.cleaned_data["Bio"]
            DateOfBirth=form.cleaned_data["DateOfBirth"]
            pic=form.cleaned_data["profilePic"]
            user = User.objects.create_user(username,email,password)
            Profile.objects.create(Name=user,username=username,bio=bio,DateOfBirth=DateOfBirth,profilePic=pic)
            user = authenticate (username = username, password=password)

            login(request,user)
        return redirect("/home")            
#wall    
def home(request):
    form = forms.PostForm()
    posts =Post.objects.all()
    
    return render(request,"Mesmerise/home.html",{"PostForm":form,"everybody":posts})    
def tPost(request):
    print('void')
    if request.method == 'POST':
        form = forms.PostForm(request.POST,request.FILES)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            tPost=form.cleaned_data["Post"]
            Pic = form.cleaned_data["Pic"]
            user = Profile.objects.get(username=request.user.username)
            Post.objects.create(post=tPost,image=Pic,author=user)
                
            return redirect("/home")
        else:
            return print("BOOM")            
def tLogin(request):
    form =  forms.LoginForm()

    return render(request,"Mesmerise/login.html",{"form":form})
def loginAction(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate (username = username, password=password)

            if user is not None:
                login(request,user)
                
                return redirect('/home')
            else:
                    
                return None                    
                