from __future__ import unicode_literals
from countryinfo.models import Address
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class ServiceProvider(models.Model):
	user=models.OneToOneField(User,related_name='provider')
	company_name = models.CharField(max_length=255,unique=True,null=False,blank=False)
	registered_address = models.CharField(max_length=255,null=False,blank=False)
	address = models.ManyToManyField(Address)
	profile_photo = models.ImageField(upload_to='', blank=True, null=True)
	service_description = models.CharField(max_length=255,blank=False,null=False)
	email_verified = models.BooleanField(default=False)
	added_on = models.DateTimeField(default=datetime.now)
	updated_on = models.DateTimeField(default=datetime.now)
	is_active= models.BooleanField(default=True)

	class Meta:
		db_table="service_provider_tbl"


class Category(models.Model):
	name=models.CharField(unique=True,max_length=100,null=False,blank=False)
	description=models.TextField(null=False,blank=False)
	added_on = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="category_tbl"


class ServiceList(models.Model):
	service_name=models.CharField(max_length=255,unique=True,blank=True,null=False)
	category=models.ForeignKey(Category)


	class Meta:
		db_table="service_list_tbl" 


class ServiceProviderRelation(models.Model):
	service_provider=models.ForeignKey(ServiceProvider)
	service_list=models.ForeignKey(ServiceList)
	created_on=models.DateTimeField(default=datetime.now)
	updated_on=models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="service_provider_relation_tbl"
		unique_together=(('service_provider','service_list'),)


class ServiceProviderFixedPayments(models.Model):
	service_provider = models.ForeignKey(ServiceProvider)
	price=models.FloatField(default=0)
	added_on = models.DateTimeField(default=datetime.now)
	updated_on=models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="service_provider_fixed_payments_tbl"
