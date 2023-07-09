from django.urls import path
from . import views

urlpatterns=[
    path('login_user/',views.login_user,name='login_user'),
    path('login_manage/',views.login_manage,name='login_manage'),
    path('category_manage/',views.category_manage,name='category_manage'),
    path('dish_manage/',views.dish_manage,name='dish_manage'),
    path('signup/',views.signup,name='signup'),
    path('add_category/',views.add_category,name='add_category'),
    path('edit_category/<int:id>',views.edit_category,name='edit_category'),
    path('delete_category/<int:id>',views.delete_category,name='delete_category'),
    path('add_dish/',views.add_dish,name='add_dish'),
    path('edit_dish/<int:id>',views.edit_dish,name='edit_dish'),
    path('delete_dish/<int:id>',views.delete_dish,name='delete_dish'),
    path('change_details/<int:id>',views.change_details,name='change_details'),
    path('user_category/',views.user_category,name='user_category'),
    path('user_dish/<int:id>',views.user_dish,name='user_dish'),
    path('main',views.main,name='main'),
    path('logout_user',views.logout_user,name='logout_user')


    
]