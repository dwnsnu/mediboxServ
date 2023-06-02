from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

import base64
import io
class Index(APIView):
    def get(self, request, format=None):
        print('hi index in docs app')
        return Response(data='hello world get!', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # print("data:image/jpg;base64,"+request.data['image']['base64'])
        decoded_data = base64.b64decode((request.data['image']['base64']))
        # data_bytes_io = io.BytesIO(image_binary)
        with open('img.jpg', 'wb') as f:
            f.write(decoded_data)
        return Response(data='hello world post!', status=status.HTTP_200_OK)
