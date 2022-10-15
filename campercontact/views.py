from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AmityCamperForm, AnthonyCamperForm
from django.core.mail import send_mail, get_connection
from django.views.generic import ListView, FormView
from .models import AmityCamperInquiry







def amitycamper(request):
    submitted = False
    if request.method == "POST":
        form = AmityCamperForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            print(data['name'],data['pickup'], data['dropoff'])
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                data['subject'],
                data['message'    ], 
                data.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/amitycamper?submitted=True')

    else:
        form = AmityCamperForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "campercontact/amitycamper.html",{'form': form, 'submitted': submitted, } )


def anthonycamper(request):
    submitted = False
    if request.method == "POST":
        form = AnthonyCamperForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            print(data['name'],data['pickup'], data['dropoff'])
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                data['subject'],
                data['message'    ], 
                data.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/anthonycamper?submitted=True')

    else:
        form = AnthonyCamperForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "campercontact/anthonycamper.html",{'form': form, 'submitted': submitted, } )







    
    



