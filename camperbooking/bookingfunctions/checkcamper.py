import datetime 
from camperbooking.models import CamperBooking, CamperBooking2
from camperinfo.models import Camper

def check_camper(camper, pickup, dropoff):
    avail_list=[]
    booking_list = CamperBooking.objects.filter(camper=camper)
    for booking in booking_list:
        if booking.pickup > dropoff or booking.dropoff < pickup:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)

def check_camper2(camper, pickup, dropoff):
    avail_list=[]
    booking_list = CamperBooking2.objects.filter(camper=camper)
    for booking in booking_list:
        if booking.pickup > dropoff or booking.dropoff < pickup:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)
