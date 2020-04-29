from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import View,APIView
from .serializers import SignateurSerializer
from .models import Signateur
from rest_framework import viewsets



# @csrf_exempt
class TestView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SignateurSerializer(data=request.data)
        print("i am in ")
        
        if serializer.is_valid():
            print("i am in 2")
            serializer.save()
            img=request.data["img_data"]
            print(img)
            return Response(serializer.data)
        return Response(serializer.errors)