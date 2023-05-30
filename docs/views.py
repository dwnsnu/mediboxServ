from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Index(APIView):
    def get(self, request, format=None):
        print('hi index in docs app')
        return Response(data='hello world!', status=status.HTTP_200_OK)
