# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from time import gmtime, strftime
from datetime import date
from django.db import models
from django import forms
import datetime
import re
import bcrypt
# MIGRATION STEPS
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# from apps.Belt_2_app.models import *

# Create your models here.


###  This section is used for validatiing User Regristerationcd
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        upper_arr='QAZWSXEDCRFVTGBYHNUJMIKOLP'
    	num_arr='1234567890'
    	EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        NAME_REGEX = re.compile(r'/^[a-zA-Z]+', re.MULTILINE)
        PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$', re.MULTILINE)

    	input_date=''
    	current_time=strftime("%Y-%m-%d", gmtime())
    	users=Fr.objects.all()

    	Z=False
    	if len(postData['birth_date'])>current_time:
    		errors['err']="Invalid Date"
        if len(postData['birth_date'])>1:
            input_date=postData['birth_date']
            year,month,day = input_date.split('-')
            Z = True
            isValidDate = True
            try:
				datetime.datetime(int(year),int(month),int(day))
            except ValueError:
				isValidDate = False
            if(isValidDate):
   				pass
            else:
                errors['err']="Invalid Date"
                Z=False
        else:
   			Z=True

        B=False
        if not PASSWORD_REGEX.match(postData['password']):
            errors['err']="Password does not meet required standard."
        else:
            B=True
        H=False
        if postData['password']!=postData['password2']:
            errors['err']="Passwords must match"
        else:
            H=True

        I=False
        if not EMAIL_REGEX.match(postData['email']):
            errors['err']="Email does not meet the standard"
        else:
            I=True

        J=False
        if NAME_REGEX.match(postData['name']):
            errors['err']="Not a valid First Name"
        else:
            J=True


        stash=[]
        # print("A ", A)
        print("B ", B)
        # print("C ", C)
        # print("D ", D)
        # print("E ", E)
        # print("F ", F)
        # print("G ", G)
        print("H ", H)
        print("I ", I)
        print("J ", J)
        # print("K", K)
        print("Z", Z)
    	if( B== True and H==True and I==True and J==True  and Z==True):
            for x in users:
                stash.append(x.email)
            if postData['email'] not in stash:
            	hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            	Fr.objects.create(name=postData['name'], alias=postData['alias'], email=postData['email'], birth_date=postData['birth_date'], password=hashed_password)
                print('success')
            else:
   				errors['err']='Sorry email in use'        	
    	return errors

###  This section is used for validatiing User Login
    def login_validator(self, postData):
        db2=Fr.objects.all()
        email=[]
        for x in db2:
            email.append(x.email)
        if(postData['email2'] in email and len(postData['password2'])!=0):
            db= Fr.objects.get(email=postData['email2'])
            if(bcrypt.checkpw(postData['password2'].encode(), db.password.encode())):
                print('ID')
                return db.id
        else:
            errors = {}
            errors['err']="Password incorrect for email given or email does not exist"
            return errors 

class Fr(models.Model):
    name=models.CharField(max_length=255)
    friends = models.ManyToManyField("self", related_name="frs")
    alias=models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birth_date=models.DateField(blank=True, default='', null=True)
    password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()





	
	# Users.objects.create(first_name="Andrew",  last_name="Rydzak", email="rydzaka12@gmail.com")










































