from django.urls import path
from account.views import SignupAPI,RestPassword
urlpatterns = [
    path('signup/',SignupAPI.as_view()),
    path('reset/',RestPassword.as_view()),
]