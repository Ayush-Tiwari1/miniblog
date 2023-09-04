from django.shortcuts import render
from .forms import SignUpForm, EditProfileForm,BlogForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.urls import reverse
def signup(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Form Submitted Successfully !!')
    else:
        fm=SignUpForm()
    return render(request,'core/signup.html',{'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request.user,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfully !!')
                    return HttpResponseRedirect(reverse('home'))
        else:
            fm=AuthenticationForm(request=request.user)
        return render(request,'core/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_profile(request):
    if request.user.is_authenticated:
        # users=None
        if request.method=="POST":
            if request.user.is_superuser:
                users=User.objects.all()
            else:
                users=None
            fm=EditProfileForm(instance=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile Updated Successfully !!')
                return HttpResponseRedirect('/home/')
        else:
            if request.user.is_superuser:
                users=User.objects.all()
            else:
                users=None
            fm=EditProfileForm(instance=request.user)
        return render(request,'core/home.html',{'name':request.user,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    if request.user.is_authenticated:
        messages.success(request,'Logout Successfully !!')
    logout(request)
    return HttpResponseRedirect('/login/')

def changepass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Password Changed Successfully !!')
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'core/changepassword.html',{'form':fm})

    else:
        return HttpResponseRedirect('/login/')


def home(request):
    
    return render(request,'core/home.html',{'is_authenticated':request.user.is_authenticated})

def about(request):
    return render(request,'core/about.html',{'is_authenticated':request.user.is_authenticated})

def contact(request):
    return render(request,'core/contact.html',{'is_authenticated':request.user.is_authenticated})

@login_required(login_url='/login/')
def dashboard(request):
    blogs=Blog.objects.all()
    return render(request,'core/dashboard.html',{'blogs':blogs,'is_authenticated':request.user.is_authenticated,'is_superuser':request.user.is_superuser,'user':request.user})


@login_required(login_url='/login/')
def addblog(request):
    if request.method=="POST":
        fm=BlogForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Blog Added Successfully !!')
            return HttpResponseRedirect('/dashboard/')
    else:
        fm=BlogForm()
    return render(request,'core/addblog.html',{'form':fm, 'is_authenticated': request.user.is_authenticated})

@login_required(login_url='/login/')
def editblog(request,id):
    user=Blog.objects.get(pk=id)
    if request.method=='POST':
        fm=BlogForm(request.POST,instance=user)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Blog Updated Successfully !!')
            return HttpResponseRedirect('/dashboard/')
    else:
        fm=BlogForm(instance=user)
    return render(request,'core/editblog.html',{'form':fm,'is_authenticated':request.user.is_authenticated})

@login_required(login_url='/login/')
def deleteblog(request,id):
    if request.user.is_superuser:
        user=Blog.objects.get(pk=id)
        user.delete()
        messages.success(request,'Blog Deleted Successfully !!')
        return HttpResponseRedirect('/dashboard/')
    else:
        messages.warning(request,'Admin can Delete Blog !!')
        return HttpResponseRedirect('/dashboard/')
