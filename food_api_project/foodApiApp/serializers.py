from rest_framework import serializers
from .models import *

class RestaurentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurentCategoryModel
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = '__all__'

