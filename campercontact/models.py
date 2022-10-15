from django.db import models

class AmityCamperInquiry(models.Model):
    camper = models.CharField(max_length=27)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pickup = models.DateTimeField()
    dropoff = models.DateTimeField()
    subject = models.CharField(max_length=27)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'camperinquiry1'
        verbose_name_plural = 'Amity Camper Inquiry'
    
    def __str__(self):
        return f' {self.name}, at {self.email}, wants to book {self.camper}, for {self. pickup}, to {self. dropoff}'



class AnthonyCamperInquiry(models.Model):
    camper = models.CharField(max_length=27)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pickup = models.DateTimeField()
    dropoff = models.DateTimeField()
    subject = models.CharField(max_length=27)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'camperinquiry2'
        verbose_name_plural = 'Anthony Camper Inquiry'
    

    def __str__(self):
        return f' {self.name}, at {self.email}, wants to book {self.camper}, for {self. pickup}, to {self. dropoff}'
