from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('camper1', views.camper1, name='camper1'),
    path('camper2', views.camper2, name='camper2'),
    path('camperadmin', views.camperadmin, name='camperadmin'),
    path('camperbooking', views.camperbooking, name='camperbooking'),
    path('camperinquiry', views.camperinquiry, name='camperinquiry'),
    path('camperrental', views.camperrental, name='camperrental'),
    path('about', views.about, name='about'),
    path('campingsitesinjapan', views.campingsites, name='campingsitesinjapan'),
    


]