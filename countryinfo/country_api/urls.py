from django.conf.urls import url
from django.contrib import admin

from .views import (
	CountryCreateAPIView,
	CountryDetailAPIView,
	CountryListAPIView,
	CountryUpdateAPIView,
	CountryDeleteAPIView
	)

urlpatterns=[
	url(r'^(?P<pk>\d+)/detail/$',CountryDetailAPIView.as_view(),name='detail'),
	url(r'^list/$',CountryListAPIView.as_view(),name='list'),
	url(r'^create/$',CountryCreateAPIView.as_view(),name='create'),
	url(r'^(?P<pk>\d+)/edit/$',CountryUpdateAPIView.as_view(),name='update'),
	url(r'^(?P<pk>\d+)/delete/$',CountryDeleteAPIView.as_view(),name='delete'),
	]