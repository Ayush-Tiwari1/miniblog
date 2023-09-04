"""
URL configuration for miniblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('',views.home,name='home'),
    path("admin/", admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('changepassword/',views.changepass,name='changepass'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('blog/',views.addblog,name='blog'),
    path('editblog/<int:id>/',views.editblog,name="editblog"),
    path('deleteblog/<int:id>/',views.deleteblog,name='deleteblog')
]
