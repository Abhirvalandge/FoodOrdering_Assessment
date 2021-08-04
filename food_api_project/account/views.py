from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.hashers import make_password

# Create your views here.

class SignupAPI(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        #print("Request=", request.data)
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED) 
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)    

class RestPassword(APIView):
    def put(self, request):
        username = request.POST.get("username")        
        old_password = request.POST.get("old_password")        
        new_password = request.POST.get("new_password")        
        new_password = make_password(new_password)
        user = User.objects.get(username=username)
        if user:
            user.password = new_password
            user.save()
            resp = {
                'success' : 'true',
                'message' : "Password Has Been Successfully Changed, You can login with new password",
            }
            return Response(resp, status=status.HTTP_201_CREATED)
        resp = {
            'success' : 'false',
            'message' : "Something went wrong try again",        }    
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)    