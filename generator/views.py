from django.shortcuts import render
from django.http import HttpResponse 
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list(string.ascii_lowercase)


    if request.GET.get('uppercase'):
        characters.extend(string.ascii_uppercase)

    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    length = int(request.GET.get('length', 12))
                             
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')