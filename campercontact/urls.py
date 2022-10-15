from django.urls import path
from . import views





urlpatterns = [

    path('amitycamper', views.amitycamper, name='amitycamper'),
    path('anthonycamper', views.anthonycamper, name='anthonycamper'),
   

]