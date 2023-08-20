from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import requests


@login_required
def exam (request)  :
    return HttpResponse('exam')

@login_required
def profile (request)  :

    url = 'http://quran.dis-store.website/surah'

    req = requests.get(url).json()


    while True : 
        
        results = req['results']

        for surah in results : 
            print(surah['id'])
            print(surah['surah_name'])
            print(surah['surah_type'])
            print(surah['number_of_ayahs'])
            print('-'*10)

        break

    return HttpResponse('profile')


def login (request) : 
    return HttpResponse('Login')


def register (request) : 
    return HttpResponse('register')

