from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    letters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        letters.extend(list('1234567890'))
    if request.GET.get('special'):
        letters.extend(list('!@#$%^%&*()_-+=?'))
    if request.GET.get('custom'):
        letters = list(request.GET.get('custom', default=''))
    
    password_length = int(request.GET.get('length'))
    for ch in range(password_length):
        thepassword += random.choice(letters) 

    return render(request, 'generator/password.html', {'password': thepassword})