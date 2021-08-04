from django.http import response
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.hashers import make_password

# Create your views here.
class SignUp(APIView):
    def post(self, request):
        print("request>>>", request.data)
        ser = UserSerializer(data = request.data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

# class ChangePasswordView(generics.UpdateAPIView):

#     #An endpoint for changing password.

#     serializer_class = ChangePasswordSerializer
#     model = User
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }

#             return Response(response)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
                    
class ResetPassword(APIView):

    def put(self, request):
        #permission_classes = (AllowAny,)
        user_name = request.POST.get('username')
        old_password = request.POST.get('old_password')
        print("username>>>>", user_name)
        print("password>>>>", old_password)
        
        new_password = request.POST.get('new_password')
        new_password = make_password(new_password)
        user = User.objects.get(username=user_name)
        if user:
            user.password = new_password
            user.save()
            resp={
                'success': 'true',
                'message': '''Password has been successfully changed, Now you can login with new password.'''
            }

            return Response(resp, status=status.HTTP_201_CREATED)

        resp = {
            'success': 'false',
            'message': 'Something went wrong please try again.'
        }

        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)