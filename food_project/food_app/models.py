from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.contrib.auth.models import User
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
    food_image = models.ImageField(upload_to='images/')
    restaurent_name = models.ForeignKey(RestaurentCategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name

class FoodOrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodModel, on_delete=models.CASCADE, default=True)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    pin_code = models.CharField(max_length=6)

    def __str__(self):
        return self.address

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.item.food_name