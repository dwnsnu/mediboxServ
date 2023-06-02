from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

import base64
class Index(APIView):
    def get(self, request, format=None):
        print('hi index in docs app')
        return Response(data='hello world get!', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # print("data:image/jpg;base64,"+request.data['image']['base64'])
        image_binary = base64.decodebytes(request.data['image']['base64'])
        with open('img.jpg', 'w') as f:
            f.write(image_binary)
        return Response(data='hello world post!', status=status.HTTP_200_OK)
