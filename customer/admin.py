from django.contrib import admin
from .models import ServiceRegistration


class ServiceRegistrationAdmin(admin.ModelAdmin):
	list_display=['user_service','service_user','service_provider']
	class Meta:
		model=ServiceRegistration

admin.site.register(ServiceRegistration,ServiceRegistrationAdmin)

