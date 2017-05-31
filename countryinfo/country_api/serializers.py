from rest_framework.serializers import (
	CharField,
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)
from datetime import datetime
from countryinfo.models import Country,State,City

class StateSerializer(ModelSerializer):
	class Meta:
		model=State
		fields=[
		'name'
		]

class CitySerializer(ModelSerializer):
	class Meta:
		model=City
		fields=[
		'name'
		]

class CountryCreateSerializer(ModelSerializer):
	#states=CharField(allow_blank=False,write_only=True)
	#city=CharField(allow_blank=False,write_only=True)
	class Meta:
		model=Country
		fields=[
			'code',
			'name',
			]


			
	

class CountryDetailSerializer(ModelSerializer):
	user=SerializerMethodField()
	class Meta:
		model=Country
		fields=[
			'id',
			'user',
			'code',
			'name',
			'added_on',
			]

class CountryUpdateSerializer(ModelSerializer):
	class Meta:
		model=Country
		fields=[
			'id',
			'user',
			'code',
			'name',
			'added_on',
			
			]
class CountryListSerializer(ModelSerializer):
	user=SerializerMethodField()
	class Meta:
		model=Country
		fields=[
			'id',
			'user',
			'code',
			'name',
			'added_on',
			]
	def get_user(self,obj):
		return str(obj.user.username)


class CountryDeleteSerializer(ModelSerializer):
	
	class Meta:
		model=Country
		fields=[
			'id',
			'user',
			'code',
			'name',
			'added_on',
			
			]