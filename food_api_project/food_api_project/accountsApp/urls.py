from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',SignUp.as_view()),
    path('api/change-password/', ResetPassword.as_view(), name='change-password')
]