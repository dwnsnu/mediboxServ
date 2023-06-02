from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

import base64
import os
from datetime import datetime

class Index(APIView):
    def get(self, request, format=None):
        print('hi index in docs app')
        return Response(data='hello world get!', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # print("data:image/jpg;base64,"+request.data['image']['base64'])
        decoded_data = base64.b64decode((request.data['image']['base64']))
        # data_bytes_io = io.BytesIO(image_binary)
        path = os.path.join(os.getcwd(), 'docs', 'media')
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        file_name = str_current_datetime + ".jpg"
        with open('docs/media/' + file_name, 'wb') as f:
            f.write(decoded_data)
        return Response(data='hello world post!', status=status.HTTP_200_OK)
