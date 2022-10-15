from django import forms

class CampercheckForm(forms.Form):

    CAMPER_CATEGORIES=(
        ('AMITY', 'Amity Camper'),
        # ('ANTHONY', 'Anthony Camper'),
        
    )

    camper_type = forms.ChoiceField(choices=CAMPER_CATEGORIES, required=True)
    booker = forms.CharField(max_length=27, required = True)
    pickup = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')
    dropoff = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')



class CampercheckForm2(forms.Form):

    CAMPER_CATEGORIES=(
        # ('AMITY', 'Amity Camper'),
        ('ANTHONY', 'Anthony Camper'),
        
    )

    camper_type = forms.ChoiceField(choices=CAMPER_CATEGORIES, required=True)
    booker = forms.CharField(max_length=27)
    pickup = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')
    dropoff = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')






