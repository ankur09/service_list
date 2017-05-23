from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.

class Country(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
	code=models.CharField(max_length=50,unique=True,null=False)
	name=models.CharField(max_length=50)
	added_on = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="country_tbl"
		verbose_name_plural='Country'

class State(models.Model):
	name=models.CharField(max_length=50,null=False,blank=False)
	

	class Meta:
		db_table="state_tbl"
		verbose_name_plural='State'

class City(models.Model):
	name=models.CharField(max_length=50,null=False,blank=False)
	

	class Meta:
		db_table="city_tbl"
		verbose_name_plural='City'

class Address(models.Model):
	country=models.ForeignKey(Country)
	state=models.ForeignKey(State)
	city=models.ForeignKey(City)
	pincode=models.CharField(max_length=10)
	street=models.CharField(max_length=255)
	addess_line1=models.CharField(max_length=255,null=True)
	addess_line2=models.CharField(max_length=255,null=True)

	class Meta:
		db_table="address_tbl"
		verbose_name_plural='Address'