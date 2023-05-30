from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Index(APIView):
    def get(self, request, format=None):
        print('hi index in docs app')
        return Response(data='hello world get!', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # tmp = request['hello']
        # print(request.data['image']['base64'])
        print("data:image/jpg;base64,"+request.data['image']['base64'])
        return Response(data='hello world post!', status=status.HTTP_200_OK)
