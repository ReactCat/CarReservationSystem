from django.db import models

class CampingSite(models.Model):
    

    campingtit1 = models.CharField(max_length=27, blank=True)
    campingarea = models.CharField(max_length=27, blank=True)
    camperimage1 = models.ImageField(upload_to='images/campingsites', blank=True)
    campingsite = models.CharField(max_length=27, blank=True)
    campingprefecture = models.CharField(max_length=27, blank=True)
    campeinginfo = models.TextField(max_length=155, blank=True)
    camperimage2 = models.ImageField(upload_to='images/campingsites', blank=True)

    class Meta:
        verbose_name = 'campingsites'
        verbose_name_plural = 'Camping Sites'



class CampingSitejpn(models.Model):
    

    campingtit1 = models.CharField(max_length=27, blank=True)
    campingarea = models.CharField(max_length=27, blank=True)
    camperimage1 = models.ImageField(upload_to='images/campingsites', blank=True)
    campingsite = models.CharField(max_length=27, blank=True)
    campingprefecture = models.CharField(max_length=27, blank=True)
    campeinginfo = models.TextField(max_length=155, blank=True)
    camperimage2 = models.ImageField(upload_to='images/campingsites', blank=True)

    class Meta:
        verbose_name = 'campingsites'
        verbose_name_plural = 'Camping Sites'