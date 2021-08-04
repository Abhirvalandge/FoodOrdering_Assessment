from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class RestaurantView(APIView):
    #List all
    def get(self, request):
        data = RestaurentCategoryModel.objects.all()
        serializer = RestaurentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Create
    def post(self, request):
        serializer = RestaurentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Update
    def put(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        mobile_no = request.POST.get('mobile_no')
        description = request.POST.get('description')
        try:
            data = RestaurentCategoryModel.objects.get(id=id)
            if data:
                data.name = name
                data.address = address
                data.mobile_no = mobile_no
                data.description = description
                data.save()
                resp={
                    'success': 'true',
                    'message': '''Restaurant has been successfully changed.'''
                }

                return Response(resp, status=status.HTTP_201_CREATED)
        except:
                resp = {
                    'success': 'false',
                    'message': 'Something went wrong please try again.'
                }
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    #Delete
    def delete(self, request):
        id = request.POST.get('id')
        try:
            data = RestaurentCategoryModel.objects.get(id=id).delete()
            resp={
                    'success': 'true',
                    'message': '''Restaurant has been successfully deleted.'''
                }

            return Response(resp, status=status.HTTP_200_OK)
        except:
                resp = {
                    'success': 'false',
                    'message': 'Something went wrong please try again.'
                }
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)


class FoodView(APIView):
    #List all
    def get(self, request):
        id = request.POST.get('id')
        data = FoodModel.objects.filter(restaurent_name=id)
        serializer = FoodSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Create
    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #update
    def put(self, request):
        id = request.POST.get('id')
        food_name = request.POST.get('food_name')
        food_price = request.POST.get('food_price')
        food_description = request.POST.get('food_description')
        food_image = request.POST.get('food_image')
        restaurent_name = request.POST.get('restaurent_name')
        data = FoodModel.objects.get(id=id)
        if data:
            data.food_name = food_name
            data.food_price = food_price
            data.food_description = food_description
            data.food_image = food_image
            data.restaurent_name = restaurent_name
            data.save()
            resp={
                'success': 'true',
                'message': '''Food Item has been successfully changed.'''
            }

            return Response(resp, status=status.HTTP_201_CREATED)

        resp = {
            'success': 'false',
            'message': 'Something went wrong please try again.'
        }

        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    #Delete
    def delete(self, request):
        id = request.POST.get('id')
        data = FoodModel.objects.get(id=id).delete()
        try:
            data = FoodModel.objects.get(id=id).delete()
            resp={
                    'success': 'true',
                    'message': '''Food Item has been successfully deleted.'''
                }

            return Response(resp, status=status.HTTP_200_OK)
        except:
                resp = {
                    'success': 'false',
                    'message': 'Something went wrong please try again.'
                }
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)