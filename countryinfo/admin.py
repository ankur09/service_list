from django.contrib import admin
from .models import (
	Country,
	State,
	City,
	
	)

class CountryAdmin(admin.ModelAdmin):
	list_display=['code','name','added_on']
	list_filter=['added_on']
	search_fields=['code','name']
	class Meta:
		model=Country

class StateAdmin(admin.ModelAdmin):
	list_display=['name']
	search_fields=['name']
	class Meta:
		model=State

class CityAdmin(admin.ModelAdmin):
	list_display=['name']
	search_fields=['name']
	class Meta:
		model=City


admin.site.register(Country,CountryAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(City,CityAdmin)
