from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import random
from .models import Surah, Ayah

@login_required
def exam (request)  :


    while True :
        ayah = random.choices(Ayah.objects.all())[0]
        
        if Ayah.objects.filter(text=ayah.text).count() == 1 :
            text = ayah.text
            surah = ayah.surah

            break
    
    all_choices = [
        random.choices(Surah.objects.all())[0].surah_name,
        random.choices(Surah.objects.all())[0].surah_name,
        random.choices(Surah.objects.all())[0].surah_name,
        surah.surah_name
    ]

    random.shuffle(all_choices)
        
    print(text)
    print(surah)
    print(all_choices)

    return HttpResponse('exam')


@login_required
def profile (request)  :
    return HttpResponse('profile')


def login (request) : 
    return HttpResponse('Login')


def register (request) : 
    return HttpResponse('register')

