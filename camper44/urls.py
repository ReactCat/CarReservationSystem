""" CAMPER RENTAL SITE MAIN URL Configuration """
from django.contrib import admin, auth
from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('camperinfo.urls')),
    path('', include('camperbooking.urls')),
    path('', include('campercontact.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

