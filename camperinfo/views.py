from django.shortcuts import render
from .models import Camper, CamperAbout, CampingSite
from django.contrib.auth.decorators import login_required

def home(request):
    camperinfo1 = Camper.objects.filter(campername='AMITY')
    camperinfo2 = Camper.objects.filter(campername='ANTHONY')
    campinginfo = CampingSite.objects.all()
   

    return render(request, "camperinfo/home.html",{
        'camperinfo1':camperinfo1,
        'camperinfo2':camperinfo2,
        'campinginfo':campinginfo,
       
    } )




def camperrental(request):
    camperinfo1 = Camper.objects.filter(campername='AMITY')
    camperinfo2 = Camper.objects.filter(campername='ANTHONY')

    return render(request, "camperinfo/camperrental.html",{
        'camperinfo1':camperinfo1,
        'camperinfo2':camperinfo2,
    } )


def camper1(request):
    camperinfo = Camper.objects.filter(campername='AMITY')
    return render(request, "camperinfo/camper1.html",{'camperinfo':camperinfo, } )

def camper2(request):
    camperinfo = Camper.objects.filter(campername='ANTHONY')
    return render(request, "camperinfo/camper2.html",{'camperinfo':camperinfo,} )

def about(request):
    aboutinfo = CamperAbout.objects.all()
    return render(request, "camperinfo/about.html",{'aboutinfo':aboutinfo,} )

def campingsites(request):
    return render(request, "camperinfo/campingsitesinjapan.html",{} )


@login_required(login_url="loginuser")
def camperadmin(request): 
    return render(request, "camperadmin/camperadmin.html",{} )


@login_required(login_url="loginuser")
def camperbooking(request): 
    return render(request, "camperadmin/camperbooking.html",{} )


@login_required(login_url="loginuser")
def camperinquiry(request): 
    return render(request, "camperadmin/camperinquiry.html",{} )



