from django import forms
from django.forms import ModelForm
from .models import AmityCamperInquiry, AnthonyCamperInquiry


class AmityCamperForm(ModelForm):
    class Meta:
        model = AmityCamperInquiry
        fields = "__all__"


class AnthonyCamperForm(ModelForm):
    class Meta:
        model = AnthonyCamperInquiry
        fields = "__all__"