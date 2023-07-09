from django.shortcuts import render,redirect
from user.models import User,Dish,Item
from .models import Cart,Order
from django.contrib.auth.decorators import login_required



list_item=[]
@login_required(login_url='login_user')
def cart(requsets,id):
    dish=Dish.objects.get(id=id)
    carts=Cart.objects.all()
    flag=False
    for item in list_item:
        if item.dish.id ==id and item.cart ==carts[len(carts)-1] : 
                item.amount=item.amount+1
                item.save()
                flag=True
    if flag==False: 
            new_item=Item()
            new_item.dish=dish
            new_item.cart=carts[len(carts)-1]
            new_item.amount=new_item.amount+1
            new_item.save()
            list_item.append(new_item)
    for item in list_item:
         if  not list_item[len(list_item)-1].cart.id==item.cart.id:
            list_item.remove(item)
    return render(requsets,'cart.html',{'list_item':list_item})




@login_required(login_url='login_user')
def order_history(request):
    orders=Order.objects.all()
    order_list=[]
    
    for order in orders:
         if order.order.user.id==request.user.id:
            order_list.append(order)
    
    return render(request,'order_history.html',{"order_list":order_list})


@login_required(login_url='login_user')
def delete(request,id):
    carts=Cart.objects.all()
    items=Item.objects.all()
    for item in items:
        if item.dish.id==id and item.cart==carts[len(carts)-1]:
            item.delete()
    for item in list_item:
         if item.dish.id==id and item.cart==carts[len(carts)-1]:
            list_item.remove(item)
            
    return render(request,'cart.html',{"list_item":list_item})

@login_required(login_url='login_user')
def order(request):
    if request.method=='POST':
           new_order=Order(
                address=request.POST['adress'],
                comment=request.POST['comment']
           )
           new_order.save()
           
           return redirect(pay)
    return render(request,'order.html')    
         
@login_required(login_url='login_user')
def pay(request): 
    total=0
    list_order=Order.objects.all()
    my_order=list_order[len(list_order)-1]
    list_item=Item.objects.all()
    carts=Cart.objects.all()
    for item in list_item:
         if item.cart==carts[len(carts)-1]:
             total+=item.amount*item.dish.price
    return render(request,'pay.html',{"total":total,'my_order':my_order})

@login_required(login_url='login_manage')
def delivery_manage(request):
     orders=Order.objects.all()
     return render(request,'delivery_manage.html',{'orders':orders})
