from django.contrib.auth import get_user_model
from django.db.models import Q 
from django.contrib.auth import authenticate
from customer.models import Customer ,ServiceRegistration
from countryinfo.country_api.serializers import StateSerializer,CitySerializer,CountryCreateSerializer
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
import hashlib
from serviceprovider.serializers import ServiceProviderSerializer
from rest_framework.serializers import (
	IntegerField,
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
from countryinfo.country_api.serializers import CountryCreateSerializer

User=get_user_model()



class RegisterSerializer(ModelSerializer):
	password2=CharField(allow_blank=False,write_only=True,label='Confirm Password')
	password=CharField(allow_blank=False,write_only=True,label='Password')
	IsServiceProvider=BooleanField(default=False,write_only=True)
	class Meta:
		model= User 
		fields = [
			'username',
			'password',
			'password2',
			'email',
			'IsServiceProvider'
			]

		read_only_fields = ['is_staff', 'is_superuser']


	def validate(self,data):
		email=data['email']	
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
		IsServiceProvider=validated_data['IsServiceProvider']
		#activation_key=validated_data['activation_key']
		user=User(
			username=username,
			email=email
			)
		user.set_password(password)
		user.save()
		service=ServiceRegistration.objects.create(user_service=user,IsServiceProvider=IsServiceProvider)
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
	IsServiceProvider=BooleanField(default=False,write_only=True)
	email=EmailField(label='Email Address',required=False,allow_blank=True)
	password=CharField(write_only=True,style={'input_type':'password'})
	class Meta:
		model= User 
		fields = [
			'email',
			'password',
			'IsServiceProvider',
			'token'
			]
		

	def validate(self,data):
		user_obj=None
		email=data.get('email')
		password=data['password']
		IsServiceProvider=data['IsServiceProvider']
		#pdb.set_trace()
		if not email and not username:
			raise ValidationError("username or email is required to login")

		user=User.objects.filter(email=email)
	
		if user.exists() and user.count()==1:
			user_obj=user.first()
		else:
			raise ValidationError("email and password is not valid")

		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Incorrect Credentials please try again")
		if user_obj.service.IsServiceProvider==IsServiceProvider :
			print "success"
		else:
			raise ValidationError("not authenticated")

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
		user_obj=None
		email=data['email']
		user=User.objects.filter(email=email).distinct()
		if user.exists() and user.count()==1:
			user_obj=user.first()
		else:
			raise ValidationError('Email address of this user is not exist so please signup')

		return user_obj

	

class PasswordSerializer(ModelSerializer):
	password2=CharField(allow_blank=False,write_only=True,label='Confirm Password')
	password=CharField(allow_blank=False,write_only=True,label='Password')
	class Meta:
		model=User
		fields=[
				'password',
				'password2'
				]

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




	

		

class UserDetailSerializer(ModelSerializer):
	class Meta:
		model=User
		fields=[
			'id'
			]

class ProfileSerializerdemo(ModelSerializer):
	user=UserDetailSerializer()
	class Meta:
		model=ServiceRegistration
		fields=[
			'user',
			'name',
			'phone',
			'address',
			'email_verified'
			]

class ChangePasswordSerializer(ModelSerializer):
	user_id=IntegerField(required=True,write_only=True,label='User id')
	old_password=CharField(required=True,write_only=True,label='Old Password')
	new_password=CharField(required=True,write_only=True,label='New Password')
	class Meta:
		model=User
		fields=[
			'user_id',
			'old_password',
			'new_password'
			]

	def validate(self,data):
		user_id=data['user_id']
		#user_id=7
		old_password=data['old_password']
		new_password=data['new_password']
		user=User.objects.filter(id=user_id).distinct()
		if user.exists():
			user_obj=user.first()

		else:
			raise ValidationError('username of particular id does not exist')

		if user_obj:
			if not user_obj.check_password(old_password):
				raise ValidationError("Incorrect old password")

		return data


class ProfileSerializer(ModelSerializer):
	user=UserDetailSerializer()
	country=CountryCreateSerializer()
	city=CitySerializer()
	state=StateSerializer()
	latitude=CharField(required=False,write_only=True)
	longitude=CharField(required=False,write_only=True)
	class Meta:
		model=ServiceRegistration
		fields=[
				'name',
				'phone',
				'country',
				'city',
				'state',
				'user',
				'latitude',
				'longitude'
				]

		

class SocialMediaLoginSerializer(ModelSerializer):
	logintype=CharField(required=True,write_only=True)
	IsServiceProvider=BooleanField(default=False,write_only=True)
	class Meta:
		model=User
		fields=[
			'username',
			'email',
			'logintype',
			'IsServiceProvider'
			]

	def validate(self,validated_data):
		username=validated_data['username']
		email=validated_data['email']
		logintype=validated_data['logintype']
		IsServiceProvider=validated_data['IsServiceProvider']
		if not email and not username:
			raise ValidationError("username and email is required to login")

		user=User.objects.filter(username=username,email=email).distinct()
		if user.exists() and user.count()==1:
			print "success"
		else:
			raise ValidationError("Email and Username not Found")

		return data