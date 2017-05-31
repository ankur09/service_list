from django.conf.urls import url
from django.contrib import admin

from .views import (
	RegisterCreateAPIView,
	RegisterListAPIView,
	UserLoginAPIView,
	ForgetPasswordAPIView,
	PasswordAPIView,
	ChangePasswordView,
	ProfileAPIView
	)

urlpatterns=[
	url(r'^create/$',RegisterCreateAPIView.as_view(),name='create'),
	url(r'^list/$',RegisterListAPIView.as_view(),name='list'),
	url(r'^login/$',UserLoginAPIView.as_view(),name='login'),
	url(r'^forget/$',ForgetPasswordAPIView.as_view(),name='forget'),
	url(r'^change/$',ChangePasswordView.as_view(),name='change_password'),
	url(r'^profile/$',ProfileAPIView.as_view(),name='profile'),
	url(r'^activation_code/(?P<activation_key>[0-9A-Za-z-]+)/(?P<service_id>\d+)',PasswordAPIView.as_view(),name='password')
	
	]