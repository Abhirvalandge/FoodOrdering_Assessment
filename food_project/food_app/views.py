from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from food_app.forms import SignUpForm, OrderForm
from django.http import HttpResponseRedirect
from django import forms
from django.utils import timezone
from django.db.models import Sum
from django.contrib import messages

# Create your views here.
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,"signup.html", {'form':form})

def logout_view(request):
    return render(request, "logout.html")

def indexView(request):
    data = RestaurentCategoryModel.objects.all()
    return render(request,'index.html',{"data":data})

@login_required
def menuView(request):
    rest = request.GET.get('id')
    data = FoodModel.objects.filter(restaurent_name=rest)
    return render(request, "menu.html", {'data':data})

def order_view(request):
    form=OrderForm()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            mobile_no = form.cleaned_data['mobile_no']
            pin_code = form.cleaned_data['pin_code']
            userOrderDetails = FoodOrderModel(user=request.user, email=email, address=address, mobile_no=mobile_no, pin_code=pin_code)
            userOrderDetails.save()
            return render(request,"successful.html")
    else: 
        return render(request,"order.html", {'form':form})  

@login_required
def add_to_cart(request, id):
    item = get_object_or_404(FoodModel, id=id)
    cart_item = CartItem.objects.create(
        item=item,
        user=request.user,
        ordered=False,
    )
    messages.info(request, "Added to Cart!!Continue Shopping!!")
    return redirect("/cart")

@login_required
def get_cart_items(request):
    cart_items = CartItem.objects.filter(user=request.user,ordered=False)
    bill = cart_items.aggregate(Sum('item__food_price'))
    number = cart_items.aggregate(Sum('quantity'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    context = {
        'cart_items':cart_items,
        'total': total,
        'count': count,
    }
    return render(request, 'cart.html', context)     



def order_item(request):
    address = request.POST.get("address")
    mobile_no = request.POST.get("mobile_no")
    pin_code = request.POST.get("pin_code")
    userOrderDetails = FoodOrderModel(user=request.user, address = address, mobile_no = mobile_no, pin_code = pin_code)
    userOrderDetails.save()
    cart_items = CartItem.objects.filter(user=request.user,ordered=False)
    ordered_date=timezone.now()
    cart_items.update(ordered = True, ordered_date = ordered_date)
    messages.info(request, "Item Ordered")
    return render(request,"successful.html")

@login_required
def delete_cart(request):
    id = request.GET.get("id")
    cart_items = CartItem.objects.filter(user=request.user,id=id).delete()
    return redirect('/cart')