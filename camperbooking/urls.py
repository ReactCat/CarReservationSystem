""" CAMPER RENTAL SITE MAIN URL Configuration """
from django.contrib import admin
from django.urls import path, include
from .views import AmityCamperInquiry, AnthonyCamperInquiry,CamperList, BookingList, BookingList2, BookingView, BookingView2



app_name='camperbooking'
# app_name='camperinfo'
# app_name='campercontact'


urlpatterns = [
    path('camperlist', CamperList.as_view(), name='camperlist'),
    path('bookinglist1', BookingList.as_view(), name='bookinglist1'),
    path('bookinglist2', BookingList2.as_view(), name='bookinglist2'),
    path('campercheck', BookingView.as_view(), name='campercheck'),
    path('campercheck2', BookingView2.as_view(), name='campercheck2'),
    path('amitycamperinquiry', AmityCamperInquiry.as_view(), name='amitycamperinquiry'),
    path('anthonycamperinquiry', AnthonyCamperInquiry.as_view(), name='anthonycamperinquiry'),
    
]