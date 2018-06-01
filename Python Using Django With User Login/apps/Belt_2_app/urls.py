# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.conf.urls import url
from . import views   
       # This line is new!

urlpatterns = [
  url(r'^main$', views.main, name='register'),
  url(r'^logout$', views.logout, name='logout_appointment'),
  # # url(r'^message$', views.message, name='the_wall_message'),
   url(r'^home$', views.home),
  url(r'^view/(?P<friend_id>\d+)$', views.view,),
  url(r'^remove/(?P<friend_id>\d+)$', views.remove, name='delete_appointment'),
  url(r'^add/(?P<friend_id>\d+)$', views.add),
  url(r'^friends$', views.friends, name='appointments_success'),
  url(r'^login$', views.login, name='the_wall_login'),
  url(r'^register$', views.register, name='appointments_register')
]