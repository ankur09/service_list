from django.contrib.auth import get_user_model
import hashlib
from customer.models import ServiceRegistration 
from rest_framework.response import Response 
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView 
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)

from .serializers import (
	RegisterSerializer,
	RegisterListSerializer,
	UserLoginSerializer,
	ForegetPasswordSerializer,
	PasswordSerializer,
	ChangePasswordSerializer,
	ProfileSerializer
	)
from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	DestroyAPIView
	)
from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError
	)
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
import pdb

User=get_user_model()

class RegisterCreateAPIView(CreateAPIView):
    serializer_class=RegisterSerializer
    queryset=ServiceRegistration.objects.all()



class RegisterListAPIView(ListAPIView):
	serializer_class=RegisterListSerializer
	queryset=User.objects.all()


class UserLoginAPIView(APIView):
	permissions_classes=[AllowAny]
	serializer_class=UserLoginSerializer

	def post(self,request,*args,**kwargs):
		data=request.data
		serializer=UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			return Response(serializer.data,status=HTTP_200_OK)
		return Response(serializer.error,status=HTTP_400_BAD_REQUEST)


class ForgetPasswordAPIView(APIView):
	#permissions_classes=[IsAuthenticated]
	serializer_class=ForegetPasswordSerializer

	def post(self,request,*args,**kwargs):
		data=request.data
		#pdb.set_trace()
		serializer=ForegetPasswordSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user=User.objects.get(email=data['email'])#use serializer field
			chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
			secret_key=get_random_string(5,chars)
			activation_key=hashlib.sha256((secret_key + user.username).encode('utf-8')).hexdigest()
			print activation_key
			service_register=ServiceRegistration.objects.select_related('activation_key').get(user_service=user)
			service_register.activation_key=activation_key
			service_register.save()
			service_register.send_email()
			return Response({'success':True})
		return Response(serializer.error,status=HTTP_400_BAD_REQUEST)


#create decorator for clicked activation link url
class PasswordAPIView(APIView):
	serializer_class=PasswordSerializer

	def post(self,request,*args,**kwargs):
		data=request.data
		#pdb.set_trace()
		serializer=PasswordSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			service_user=ServiceRegistration.objects.filter(activation_key__icontains=kwargs['activation_key'],id=kwargs['service_id']).distinct()
			if service_user.exists() and service_user.count()==1:
				service_user=service_user.first()
				service_user.email_verified=True
				service_user.save()
				return Response({'success':True})
				
			else:
				return Response({'Status':'Failed'})
				

class ChangePasswordView(APIView):
	serializer_class=ChangePasswordSerializer

	def post(self,request,*args,**kwargs):
		data=request.data
		serializer=ChangePasswordSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user=User.objects.filter(id=serializer.validated_data['user_id']).distinct()
			if user.exists() and user.count()==1:
				user_obj=user.first()
			if user_obj:
				user_obj.set_password(serializer.validated_data['new_password'])
				user_obj.save()
				return Response({'success':True})
			else:
				return Response({'status':False})


class ProfileAPIView(APIView):
	serializer_class=ProfileSerializer

	def post(self,request,*args,**kwargs):
		data=request.data
		serializer=ProfileSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			return Response({'success':True})
		else:
			return Response({'status':False})