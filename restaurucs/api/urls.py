#-*- coding: utf-8 -*-
from django.urls import path
from api import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
]
