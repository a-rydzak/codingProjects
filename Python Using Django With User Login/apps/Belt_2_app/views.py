# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from django.utils.datastructures import MultiValueDictKeyError
from .models import *
import datetime
from datetime import date
from datetime import datetime
import bcrypt
import random

#To Start, go to cd.. apps
#python ../manage.py runserver
####



###  This is the the route for the index page.  This loads the login and regristration forms and initializes the sessions
def main(request):

    if 'id' not in request.session:
        request.session['id']=''
    if 'name' not in request.session:
        request.session['name']=''
    if 'success_message' not in request.session:
    	request.session['success_message']=''
    return render(request, 'Belt_2_app/index.html')

###  Route that registers a new user
def register(request):
    errors = Fr.objects.basic_validator(request.POST)
    if len(errors):
		result={}
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect(request, 'Belt_2_app/index.html')
    else:
        request.session['activity']=[]
        request.session['success_message']='Successful Registration Now log in'
        print(len(errors))
        return redirect('/main')
    return redirect('/main') 



###  Route that takes logs in a registered user
def login(request):
    errors = Fr.objects.login_validator(request.POST)
    if isinstance(errors, int):
        ID=Fr.objects.login_validator(request.POST)
        user=Fr.objects.get(id=ID)
        request.session['id']=user.id
        return redirect('/friends')
    elif len(errors):
        result={}
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return render(request, 'Belt_2_app/index.html')
    return redirect('/main')


###  Logs the user out and clears the session
def logout(request):
	# https://docs.djangoproject.com/en/2.0/topics/http/sessions/
	request.session.clear()
	request.session.pop()
    # request.session['id']=''
    # request.session['name']=''
    # request.session['success_message']=''
    return redirect('/main')


def add(request, friend_id):
    friend= Fr.objects.get(id=request.session['id'])
    friend.friends.add(friend_id)
    return redirect('/friends')

def remove(request, friend_id):
    friend= Fr.objects.get(id=request.session['id'])
    friend.friends.remove(friend_id)
    return redirect('/friends')

def view(request, friend_id):
    friend= Fr.objects.get(id=friend_id)
    return render(request,'Belt_2_app/view.html', {'friend':friend})
def home(request):
    return redirect('/friends')
###  The main page that holds the loggen in users appointments
def friends(request):
    friend= Fr.objects.get(id=request.session['id'])
    all_friends=friend.friends.all()

    non_friends=Fr.objects.all().exclude(id=request.session['id'])
    non_friends2=non_friends.difference(all_friends)


    return render(request,'Belt_2_app/friends.html', {'friend':friend, 'all_friends': all_friends,'non_friends2': non_friends2})








