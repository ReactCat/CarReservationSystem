from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


# def signupuser(request): 
#     if request.method == 'GET':
#         return render(request, "accounts/signup.html",{'form': UserCreationForm()} )
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('camperadmin')
#             except IntegrityError:
#                 return render(request, "accounts/signup.html",{'form': UserCreationForm(), 'error': 'User already exists'} )



#         else:
#             return render(request, "accounts/signup.html",{'form': UserCreationForm(), 'error': 'Passwords Did Not Match'} )


def loginuser(request): 
    if request.method == 'GET':
        return render(request, "accounts/login.html",{'form': (AuthenticationForm)} )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request, "accounts/login.html",{'form': (AuthenticationForm), 'error': 'Username and password not correct'} )
        else:
            login(request, user)
            return redirect('camperadmin')

       



        
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('camperadmin')

    
           


    



