from django.urls import path,include
from food_app import views

urlpatterns = [
     path('', views.indexView),   
     path('menuView/', views.menuView, name='menuView'),  
     path('signup_view/',views.signup_view, name='signup_view'),
     path('order_view/',views.order_view, name='order_view'), 
     path('order_item/',views.order_item, name='order_item'), 
     path('accounts/', include('django.contrib.auth.urls')),
     path('logout/', views.logout_view),
     path('add-to-cart/<int:id>/', views.add_to_cart, name='add-to-cart'),
     path('cart/', views.get_cart_items, name='cart'),
     path('delete_cart/', views.delete_cart, name='delete_cart'),

]