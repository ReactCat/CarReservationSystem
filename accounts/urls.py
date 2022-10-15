from django.urls import path
from django.contrib import auth
from . import views



urlpatterns = [

   
    # path('signup', views.signupuser, name='signupuser'),
    path('login', views.loginuser, name='loginuser'),
    path('logout', views.logoutuser, name='logoutuser'),
    

    
    
   
    

]