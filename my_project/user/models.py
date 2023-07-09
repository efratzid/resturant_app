from django.db import models
from order.models import Cart


class User(models.Model):
    
    user_name=models.CharField(max_length=200, default="")
    password=models.CharField(max_length=5)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    is_staff=models.BooleanField(default=False)
    email=models.EmailField()

class Category(models.Model):
        name=models.CharField(max_length=50)
        imageUrl=models.CharField(max_length=200)


class Dish(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    imageUrl=models.CharField(max_length=200)
    is_gloten_free=models.BooleanField(default=False)
    is_vegetarian=models.BooleanField(default=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    

class Item(models.Model):
       dish=models.ForeignKey(Dish,default="",on_delete=models.CASCADE)
       cart=models.ForeignKey(Cart,default="", on_delete=models.CASCADE)
       amount=models.IntegerField(default=0)

          

