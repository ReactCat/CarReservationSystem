from django.db import models
from django.conf import settings 
from camperinfo.models import Camper


class CamperBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    camper = models.ForeignKey(Camper, on_delete=models.CASCADE)
    booker = models.CharField(max_length=27, blank=True)
    pickup = models.DateTimeField()
    dropoff = models.DateTimeField()

    class Meta:
        verbose_name = 'camperbooking'
        verbose_name_plural = 'Camper Booking Amity'

    def __str__(self):
        return f' {self.camper} is booked by {self.booker} from {self.pickup} to {self.dropoff} '

class CamperBooking2(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    camper = models.ForeignKey(Camper, on_delete=models.CASCADE)
    booker = models.CharField(max_length=27, blank=True)    
    pickup = models.DateTimeField()
    dropoff = models.DateTimeField()

    class Meta:
        verbose_name = 'camperbooking'
        verbose_name_plural = 'Camper Booking Anthony'

    def __str__(self):
        return f' {self.camper} is booked by {self.booker} from {self.pickup} to {self.dropoff} '
