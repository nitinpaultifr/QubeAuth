from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from authapi import views

urlpatterns = [	
	url(r'^$', views.APIRootView.as_view(), name='api-root'),
	url(r'^auth/', views.AuthView.as_view(), name='auth-views'),
	url(r'^userdetails/', views.UserDetailsView.as_view(), name='user-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)