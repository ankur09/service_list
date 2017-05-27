from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from countryinfo.models import Country,Address
from django.conf import settings
from django.core.mail import send_mail
# Create your models here.

class Customer(models.Model):
	country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country',blank=True,null=True)
	name = models.CharField(max_length=50,blank=True,null=True)
	phone = models.CharField(max_length=20,unique=True,blank=True,null=True)
	address = models.ManyToManyField(Address)
	profile_photo = models.ImageField(upload_to='', blank=True, null=True) #give the image path
	email_verified = models.BooleanField(default=False)
   	added_on = models.DateTimeField(default=datetime.now)
	updated_on = models.DateTimeField(default=datetime.now)
	is_active= models.BooleanField(default=True)

	class Meta:
		abstract=True



class ServiceRegistration(Customer):
	user_service=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='service')
	service_user=models.BooleanField(default=False)
	service_provider=models.BooleanField(default=False)
	activation_key=models.CharField(max_length=120,blank=True,null=True)
	key_expires=models.DateTimeField(default=datetime.now)

	class Meta:
		db_table="service_registered"

	def __unicode__(self):
		return self.user_service.username

	def json_data(self):
		d={'service_name':self.user_service.username,'email':self.user_service.email}
		return d

	def send_email(self):
		if self.activation_key is not None :
			subject='activation link'
			link='http://127.0.0.1:8000/api/customer/activation_code/%s/%s/' %(self.activation_key,self.id)
			from_email=settings.EMAIL_HOST_USER
			to_email=[from_email,self.user_service.email]
			return send_mail(subject,link,from_email,to_email,fail_silently=False)

