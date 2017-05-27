from django.conf.urls import url
from django.contrib import admin

from .views import (
	RegisterCreateAPIView,
	RegisterListAPIView,
	UserLoginAPIView,
	)

urlpatterns=[
	url(r'^create/$',RegisterCreateAPIView.as_view(),name='create'),
	url(r'^list/$',RegisterListAPIView.as_view(),name='list'),
	url(r'^login/$',UserLoginAPIView.as_view(),name='login'),
	#url(r'^activation/(?P<activation_key>[0-9A-Za-z-]+)',)
	
	]