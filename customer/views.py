from django.shortcuts import render
from django.contrib.auth.models import User
import hashlib
from django.utils.crypto import get_random_string
from datetime import datetime,timedelta
from .models import ServiceRegistration



def generate_activation_key(username):
	chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	secret_key=get_random_string(20,chars)
	return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()


def activation_link(request,user_id):
	data={}
	user=User.objects.get(id=user_id)
	if user is not None and not user.is_active:
		data['username']=user.username
		data['email']=user.email
		data['email_subject']='password_activation'
		data['activation_key']=generate_activation_key(user.username)
		user.service.activation_key=data['activation_key']
		user.service.key_expires=datetime.strftime(datetime.now()+timedelta(days=2),'%Y-%m-%d %H:%M:%S')
		user.save()
		#send email


		

