from django.db import models

class Camper(models.Model):
    CAMPER_CATEGORIES=(
        ('AMITY', 'Amity Camper'),
        ('ANTHONY', 'Anthony Camper'),
        
    )

    campername = models.CharField(max_length=7, choices=CAMPER_CATEGORIES)
    camperinfo = models.TextField(max_length=155, blank=True)
    camperinfo2 = models.TextField(max_length=255, blank=True)
    camperprice = models.DecimalField(max_digits=8, decimal_places=0, default=0,)
    maker = models.CharField(max_length=25)
    transmission = models.CharField(max_length=25)
    wheeldrive = models.CharField(max_length=25)
    carnavi = models.CharField(max_length=25,  blank=True)
    passenger = models.IntegerField()
    petsok = models.CharField(max_length=25,  blank=True)
    camperimage = models.ImageField(upload_to='images/camperinfo', blank=True)
    
    class Meta:
        verbose_name = 'camper'
        verbose_name_plural = 'Camper '
    

    def __str__(self):
        return f'{self.campername}, Rental Campervan '


class Camperjpn(models.Model):
    CAMPER_CATEGORIES=(
        ('AMITY', 'Amity Camper'),
        ('ANTHONY', 'Anthony Camper'),
        
    )

    campername = models.CharField(max_length=7, choices=CAMPER_CATEGORIES)
    camperinfo = models.TextField(max_length=155, blank=True)
    camperinfo2 = models.TextField(max_length=255, blank=True)
    camperprice = models.DecimalField(max_digits=8, decimal_places=0, default=0,)
    maker = models.CharField(max_length=25)
    transmission = models.CharField(max_length=25)
    wheeldrive = models.CharField(max_length=25)
    carnavi = models.CharField(max_length=25,  blank=True)
    passenger = models.IntegerField()
    petsok = models.CharField(max_length=25,  blank=True)
    camperimage = models.ImageField(upload_to='images/camperinfo', blank=True)
    
    class Meta:
        verbose_name = 'camperjpn'
        verbose_name_plural = 'Camper Jpn'
    

    def __str__(self):
        return f'{self.campername}, Rental Campervan '



class CampingSite(models.Model):  

    campingtit1 = models.CharField(max_length=27, blank=True)
    campinginfo1 = models.CharField(max_length=77, blank=True)
    camperimage1 = models.ImageField(upload_to='images/campingsites', blank=True)
   
    campingtit2 = models.CharField(max_length=27, blank=True)
    campinginfo2 = models.CharField(max_length=77, blank=True)
    camperimage2 = models.ImageField(upload_to='images/campingsites', blank=True)

    campingtit3 = models.CharField(max_length=27, blank=True)
    campinginfo3 = models.CharField(max_length=77, blank=True)
    camperimage3 = models.ImageField(upload_to='images/campingsites', blank=True)
   
    class Meta:
        verbose_name = 'campingsites'
        verbose_name_plural = 'Camping Site Info'


class CampingSitejpn(models.Model):
    
    campingtit1 = models.CharField(max_length=27, blank=True)
    campinginfo1 = models.CharField(max_length=77, blank=True)
    camperimage1 = models.ImageField(upload_to='images/campingsites', blank=True)
   
    campingtit2 = models.CharField(max_length=27, blank=True)
    campinginfo2 = models.CharField(max_length=77, blank=True)
    camperimage2 = models.ImageField(upload_to='images/campingsites', blank=True)

    campingtit3 = models.CharField(max_length=27, blank=True)
    campinginfo3 = models.CharField(max_length=77, blank=True)
    camperimage3 = models.ImageField(upload_to='images/campingsites', blank=True)
   
    class Meta:
        verbose_name = 'campingsitesjpn'
        verbose_name_plural = 'Camping Site Info jpn'






class CamperAbout(models.Model):

    maindesc = models.TextField(max_length=777, blank=True)
    
    tit1 = models.CharField(max_length=25, blank=True)
    content1 = models.TextField(max_length=255, blank=True)

    tit2 = models.CharField(max_length=25, blank=True)
    content2 = models.TextField(max_length=255, blank=True)

    tit3 = models.CharField(max_length=25, blank=True)
    content3 = models.TextField(max_length=255, blank=True)

    tit4 = models.CharField(max_length=25, blank=True)
    content4 = models.TextField(max_length=255, blank=True)


    class Meta:
        verbose_name = 'camperabout'
        verbose_name_plural = 'About Info'
    


class CamperAboutjpn(models.Model):

    maindesc = models.TextField(max_length=777, blank=True)

    tit1 = models.CharField(max_length=25, blank=True)
    content1 = models.TextField(max_length=255, blank=True)

    tit2 = models.CharField(max_length=25, blank=True)
    content2 = models.TextField(max_length=255, blank=True)

    tit3 = models.CharField(max_length=25, blank=True)
    content3 = models.TextField(max_length=255, blank=True)

    tit4 = models.CharField(max_length=25, blank=True)
    content4 = models.TextField(max_length=255, blank=True)



    class Meta:
        verbose_name = 'camperaboutjpn'
        verbose_name_plural = 'About Info Jpn'