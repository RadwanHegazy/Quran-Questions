from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import random, uuid
from .models import Surah, Ayah, LeaderboardModel
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login

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

    # top 10 leaders
    leaders = LeaderboardModel.objects.order_by('-points')[:10]


    return HttpResponse('profile')


def login (request) : 
    return HttpResponse('Login')


def register (request) : 

    if request.method == "POST" : 
        name = request.POST['name']
        username = f'{str(name).replace("","_")}|{uuid.uuid4()}'
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password
        )

        user.first_name = name
        
        user.save()

        auth_login(request,user)


    return HttpResponse('register')

