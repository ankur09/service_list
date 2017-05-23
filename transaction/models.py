from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from customer.models import Customer
from serviceprovider.models import ServiceProviderRelation
# Create your models here

class CustomerBooking(models.Model):
	customer = models.ForeignKey(Customer)
	service_provider = models.ForeignKey(ServiceProviderRelation)
	added_on = models.DateTimeField(default=datetime.now)


	class Meta:
		db_table ="customer_booking_tbl"


class Transaction(models.Model):
	customer_booking=models.ForeignKey(CustomerBooking)
	amount=models.FloatField(default=0)
	added_on = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="transaction_tbl"




