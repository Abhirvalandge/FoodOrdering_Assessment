from django.urls import path
from .views import *

urlpatterns = [
        path('restaurant-view/', RestaurantView.as_view()),    
        path('food-view/', FoodView.as_view()),    
]
