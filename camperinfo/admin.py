from django.contrib import admin

from .models import Camper, Camperjpn, CamperAbout, CamperAboutjpn, CampingSite, CampingSitejpn


admin.site.register(Camper)
admin.site.register(Camperjpn)
admin.site.register(CamperAbout)
admin.site.register(CamperAboutjpn)
admin.site.register(CampingSite)
admin.site.register(CampingSitejpn)

