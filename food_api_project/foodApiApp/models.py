from django.db import models
from account.models import User
from django.utils import timezone

# Create your models here.
class RestaurentCategoryModel(models.Model):
    name  = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class FoodModel(models.Model):
    food_name = models.CharField(max_length=100)
    food_price = models.IntegerField()
    food_description = models.CharField(max_length=500)
    restaurent_name = models.ForeignKey(RestaurentCategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name



