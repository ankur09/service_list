from __future__ import unicode_literals

from django.db import models
from customer.models import Customer
from serviceprovider.models import ServiceProviderRelation
from datetime import datetime
# Create your models here.


class Rating(models.Model):
	customer = models.ForeignKey(Customer)
	service_provider = models.ForeignKey(ServiceProviderRelation)
	rating=models.FloatField(default=0)
	added_on = models.DateTimeField(default=datetime.now)
	updated_on=models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="rating_tbl"


class Review(models.Model):
	customer = models.ForeignKey(Customer)
	service_provider = models.ForeignKey(ServiceProviderRelation)
	review=models.CharField(max_length=255)
	added_on = models.DateTimeField(default=datetime.now)
	updated_on=models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="review_tbl"