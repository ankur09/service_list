from django.contrib.auth import get_user_model
from django.db.models import Q 
from django.contrib.auth import authenticate
from customer.models import Customer ,ServiceRegistration
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from rest_framework.serializers import (
	BooleanField,
	EmailField,
	CharField,
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError,
	SerializerMethodField
	)
from datetime import datetime
import pdb

User=get_user_model()



class RegisterSerializer(ModelSerializer):
	password2=CharField(allow_blank=False,write_only=True,label='Confirm Password',style={'input_type':'password'})
	password=CharField(allow_blank=False,write_only=True,label='Password',style={'input_type':'password'})
	service_user=BooleanField(default=False,write_only=True)
	service_provider=BooleanField(default=False,write_only=True)
	class Meta:
		model= User 
		fields = [
			'username',
			'password',
			'password2',
			'email',
			'service_user',
			'service_provider'
			]

		read_only_fields = ['is_staff', 'is_superuser']


	def validate(self,data):
		email=data['email']
		service_user=data['service_user']
		service_provider=data['service_provider']
		if service_provider == service_user:
			raise ValidationError("Select one of the field")
			
		user_qs=User.objects.filter(email=email)
		if user_qs:
			raise ValidationError("This user Email is already Registered")
		#if data['password']!=data.pop('password2'):
		#	raise ValidationError("Password must match")


		return data

	def validate_password(self,value):
		data=self.get_initial()
		password=data.get('password')
		password2=value
		if password!=password2:
			raise ValidationError("Password must match")
		return value

	def validate_password2(self,value):
		data=self.get_initial()
		password=data.get('password')
		password2=value
		if password!=password2:
			raise ValidationError("Password must match")
		return value

	def create(self,validated_data):
		username=validated_data['username']
		email=validated_data['email']
		password=validated_data['password']
		service_user=validated_data['service_user']
		service_provider=validated_data['service_provider']
		activation_key=validated_data['activation_key']
		user=User(
			username=username,
			email=email
			)
		user.set_password(password)
		user.save()
		service=ServiceRegistration.objects.create(user_service=user,service_user=service_user,service_provider=service_provider,activation_key=activation_key,key_expires=datetime.strftime(datetime.now()+timedelta(days=2),"%Y-%m-%d %H:%M:%S"))
		service.save()
		return user


class RegisterListSerializer(ModelSerializer):
	class Meta:
		model= User 
		fields = [
			'username',
			'password',
			'email'
			]


class UserLoginSerializer(ModelSerializer):
	token=CharField(allow_blank=True,read_only=True)
	service_provider=BooleanField(default=False,write_only=True)
	service_user=BooleanField(default=False,write_only=True)
	username=CharField(required=False,allow_blank=True)
	email=EmailField(label='Email Address',required=False,allow_blank=True)
	password=CharField(write_only=True,style={'input_type':'password'})
	class Meta:
		model= User 
		fields = [
			'username',
			'email',
			'password',
			'service_user',
			'service_provider',
			'token'
			]
		

	def validate(self,data):
		user_obj=None
		email=data.get('email')
		username=data.get("username",None)
		password=data['password']
		service_user=data['service_user']
		service_provider=data['service_provider']
		#pdb.set_trace()
		if service_provider==service_user:
			raise ValidationError("Select only one field ")
		if not email and not username:
			raise ValidationError("username or email is required to login")

		user=User.objects.filter(Q(username=username)| Q(email=email)).distinct()
		user=user.exclude(email__isnull=True).exclude(email__iexact='')
		if user.exists() and user.count()==1:
			user_obj=user.first()
		else:
			raise ValidationError("username and password is not valid")

		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Incorrect Credentials please try again")
		if user_obj.service.service_user==service_user and user_obj.service.service_provider==service_provider:
			print "success"
		else:
			raise ValidationError("Incorrect selection field")

		data['token']="anfaflfafja"
		return data


class ForegetPasswordSerializer(ModelSerializer):
	email=CharField(label='Email address',required=True,write_only=True)
	class Meta:
		model=User
		fields=[
				'email'
				]

	def validate(self,data):
		email=data['email']
		user=User.objects.get(email=email)
		if not user:
			raise ValidationError('Email address of this user is not exist')
		return data


	
		


