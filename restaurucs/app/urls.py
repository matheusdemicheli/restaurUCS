#-*- coding: utf-8 -*-
from django.urls import path
from app import views


urlpatterns = [
    path('',
         views.IndexView.as_view(),
         name='index'),

    path('estabelecimento/<int:pk>/',
         views.HomeEstabelecimentoView.as_view(),
         name='home_estabelecimento')
]
