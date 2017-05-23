from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from countryinfo.models import Country,Address
from django.conf import settings
# Create your models here.

class Customer(models.Model):
	country=models.ForeignKey(Country)
	name = models.CharField(max_length=50,blank=False,null=False)
	phone = models.CharField(max_length=20,unique=True,blank=False,null=False)
	address = models.ManyToManyField(Address)
	email = models.CharField(max_length=50,unique=True,blank=False,null=False)
	profile_photo = models.ImageField(upload_to='', blank=True, null=True) #give the image path
	password = models.CharField(max_length=30, null=True,blank=True)
	email_verified = models.BooleanField(default=False)
   	added_on = models.DateTimeField(default=datetime.now)
	updated_on = models.DateTimeField(default=datetime.now)
	is_active= models.BooleanField(default=True)

	class Meta:
		db_table="customer_tbl"

class ServiceRegistration(models.Model):
	user_service=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='service')
	service_user=models.BooleanField(default=False)
	service_provider=models.BooleanField(default=False)

	class Meta:
		db_table="service_registered"
