from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class APIRootView(APIView):
	"""
	API Root for the QubeAuth authentication API.
	"""
	def get(self, request, format=None):
		message_dump = {
			'message': 'You are here: API Root.',
		}
		data = json.dumps(message_dump)
		return Response(data, content_type='application/json')

class AuthView(APIView):
	"""
	API endpoint to generate auth token for a remote client.
	"""
	def get(self, request, format=None):
		message_dump = {
			'message': 'POST credentials to generate auth token.',
		}
		data = json.dumps(message_dump)
		return Response(data, content_type='application/json')

	def post(self, request, format=None):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				message = 'Remote client authenticated.'
		else:
			newremote = User.objects.create_user(username, None, password)
			newremote.save()
			user = authenticate(username=username, password=password)
			if user.is_active:
				login(request, user)
				message = 'New remote client added & authenticated.'

		token = Token.objects.get_or_create(user=user)

		message_dump = {
			'message': message,
			'Token': token[0].key
		}
		data = json.dumps(message_dump)
		return Response(data, content_type='application/json')

class UserDetailsView(APIView):
	"""
	API endpoint for retrieving user details of a user.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		return Response({'detail': "You are authenticated."})