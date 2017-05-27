from django.contrib.auth import get_user_model

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
	UserLoginSerializer
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



