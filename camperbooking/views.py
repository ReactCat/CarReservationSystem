from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, FormView
from .models import CamperBooking, CamperBooking2
from camperinfo.models import Camper
from campercontact.models import AmityCamperInquiry, AnthonyCamperInquiry

from .forms import CampercheckForm, CampercheckForm2
from camperbooking.bookingfunctions.checkcamper import check_camper


class CamperList(ListView):
    model = Camper

class AmityCamperInquiry(ListView):
    model = AmityCamperInquiry

class AnthonyCamperInquiry(ListView):
    model = AnthonyCamperInquiry


class BookingList(ListView):
    model = CamperBooking

class BookingList2(ListView):
    model = CamperBooking2

class BookingView(FormView):
    form_class = CampercheckForm
    template_name = 'camperbooking/campercheck.html'

    def form_valid(self, form):
        data = form.cleaned_data
        camper_list = Camper.objects.filter(campername = data['camper_type'])
        

        available_camper = []
        for camper in camper_list:
            if check_camper(camper, data['pickup'], data['dropoff']):
                available_camper.append(camper)

        if len(available_camper) >0:
            camper = available_camper[0]
            booking = CamperBooking.objects.create(
            user = self.request.user, 
            camper = camper, 
            booker = data['booker'],
            pickup = data['pickup'],
            dropoff = data['dropoff'],

            )
            booking.save()
            return HttpResponse(booking)

        else:
            return HttpResponse('Sorry, this camper is alredy booked for that time. Please try another time or send us an inquiry.  ')
        

class BookingView2(FormView):
    form_class = CampercheckForm2
    template_name = 'camperbooking/campercheck2.html'

    def form_valid(self, form):
        data = form.cleaned_data
        camper_list = Camper.objects.filter(campername = data['camper_type'])
        

        available_camper = []
        for camper in camper_list:
            if check_camper(camper, data['pickup'], data['dropoff']):
                available_camper.append(camper)

        if len(available_camper) >0:
            camper = available_camper[0]
            booking = CamperBooking2.objects.create(
            user = self.request.user, 
            camper = camper, 
            booker = data['booker'],
            pickup = data['pickup'],
            dropoff = data['dropoff'],

            )
            booking.save()
            return HttpResponse(booking)

        else:
            return HttpResponse('Sorry, this camper is alredy booked for that time. Please try another time or send us an inquiry.  ')
        