from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from authapi import views

urlpatterns = [	
	url(r'^', views.APIRootView.as_view(), name='api-root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)