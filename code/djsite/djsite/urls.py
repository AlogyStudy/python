"""djsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse, render
from app import views


urlpatterns = [
    url(r'^login/', views.login),
    url(r'^json_data/', views.json_data)
    # url(r'^press_list/', views.press_list),
    # url(r'^add_list/', views.add_list),
    # url(r'^del_list/', views.del_list),
    # url(r'^edit_press/', views.edit_press),
    # url(r'^book_list/', views.book_list),
    # url(r'^author_list/', views.author_list),
    # url(r'^upload/', views.upload)
    # url(r'/', home)
]
