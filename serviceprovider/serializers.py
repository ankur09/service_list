from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q 
from django.contrib.auth import authenticate
from .models import ServiceProvider,Category,ServiceList
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

User=get_user_model()

class ServiceProviderSerializer(ModelSerializer):
	class Meta:
		model=ServiceProvider
		fields=[
				'company_name',
				'service_description',
				'registered_address',
				]
