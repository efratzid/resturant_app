from django.shortcuts import render,redirect
from .models import Category
from .models import Dish
from order.models import Cart
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


def main(request):
    return render(request,'main.html')

def signup(request):
    if request.method=='POST':
        is_staff=request.POST.get('is_staff')=='on'
        new_user=User(
           username=request.POST['username'],
           password=make_password(request.POST['password']),
           first_name=request.POST['firstname'],
           last_name=request.POST['lastname'],
           is_staff=is_staff,
           email=request.POST['email'],
        )
        new_user.save()
        if request.POST.get('is_staff')=='on':
            return redirect('login_manage')
        return redirect('login_user')
    return render(request,'signup.html')

def login_user(request):
    if request.user.is_authenticated:
        new_cart=Cart(user_id=request.user.id)   
        new_cart.save()
        return redirect('user_category')
    if request.method == "POST":
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is not None:
            login(request,user)
            new_cart=Cart(user_id=request.user.id)   
            new_cart.save()
            return redirect('user_category')
        else:
            return HttpResponse('login failed')
    return render(request,'login_user.html')

 
def login_manage(request):
    if request.user.is_authenticated:
        return redirect('category_manage')
    if request.method == "POST":
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is not None:
            login(request,user)
            return redirect("category_manage")
        else:
            return HttpResponse('login failed')
    return render(request,'login_manage.html')


@login_required(login_url=main)
def logout_user(request):
    logout(request)
    return redirect('main')

@login_required(login_url=login_manage)
def category_manage(request):
    categories=Category.objects.all()
    return render(request,'category_manage.html',{'category_list':categories})

@login_required(login_url=login_manage) 
def add_category(request):
    if request.method=='POST':
        new_category=Category(
           name=request.POST['name'],
           imageUrl=request.POST['imageUrl'] 
        )
        new_category.save()
        return redirect(category_manage)
    return render(request,'add_category.html')

@login_required(login_url=login_manage) 
def edit_category(request,id):
    category=Category.objects.get(id=id)
    if request.method=='POST':
        category.name=request.POST['name']
        category.imageUrl=request.POST['imageUrl']
        category.save()
        return redirect(category_manage)
    return render(request,'edit_category.html',{"category":category})

@login_required(login_url=login_manage) 
def delete_category(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    return redirect(category_manage)
    

@login_required(login_url=login_user) 
def dish_manage(request):
    dish=Dish.objects.all()
    return render(request,'dish_manage.html',{"dishes":dish})

@login_required(login_url=login_manage)
def add_dish(request):
    is_gloten_free=request.POST.get('is_gloten_free')=='on'
    is_vegetarian=request.POST.get('is_vegetarian')=='on'
    if request.method=='POST':
        new_dish=Dish(
            name=request.POST['name'],
            price=request.POST['price'],
            description=request.POST['description'],
            imageUrl=request.POST['imageUrl'],
            is_gloten_free=is_gloten_free,
            is_vegetarian=is_vegetarian,
            category_id=request.POST['categories']
        )
        new_dish.save()
        return redirect(dish_manage)
    categories=Category.objects.all()
    return render(request,'add_dish.html',{"categories":categories})

@login_required(login_url=login_manage)
def delete_dish(request,id):
    dish=Dish.objects.get(id=id)
    dish.delete()
    return redirect(dish_manage)
   
@login_required(login_url=login_manage)
def edit_dish(request,id):
    dish=Dish.objects.get(id=id)
    categories=Category.objects.all()
    if request.method=='POST':
        dish.name=request.POST['name']
        dish.price=request.POST['price']
        dish.description=request.POST['description']
        dish.imageUrl=request.POST['imageUrl']
        dish.is_gloten_free=request.POST.get('is_gloten_free',False)
        dish.is_vegetarian=request.POST.get('is_vegetarian',False)
        dish.category.name=request.POST['categories']    
        dish.save()
        return redirect(dish_manage)
    return render(request,'edit_dish.html',{"dish":dish,'categories':categories})

@login_required(login_url=login_user)
def change_details(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.password=request.POST['password']
        user.username=request.POST['username']
        user.is_staff=user.is_staff
        user.email=request.POST['email']
        user.save()
        return redirect(user_category)
    return render(request,'change_details.html',{'user':user})

@login_required(login_url=login_user)
def user_category(request):
    categories=Category.objects.all()
    return render(request,'user_category.html',{'category_list':categories})

@login_required(login_url=login_user)
def user_dish(request,id):
    category=Category.objects.get(id=id)
    dishes=Dish.objects.all()
    return render(request,'user_dish.html',{'category':category,'dishes_list':dishes})
    
