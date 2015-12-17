from django.shortcuts import render
import json

from rest_framework.views import APIView
from rest_framework.response import Response

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