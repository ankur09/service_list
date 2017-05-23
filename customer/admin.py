from django.contrib import admin
from .models import Customer,ServiceRegistration

class CustomerAdmin(admin.ModelAdmin):
	list_display=['name','phone','email_verified','added_on','updated_on','is_active']
	list_filter=['name','phone']
	search_fields=['name','phone']
	class Meta:
		model=Customer

class ServiceRegistrationAdmin(admin.ModelAdmin):
	list_display=['user_service','service_user','service_provider']
	class Meta:
		model=ServiceRegistration

admin.site.register(Customer,CustomerAdmin)
admin.site.register(ServiceRegistration,ServiceRegistrationAdmin)

