from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import random, uuid
from .models import Surah, Ayah, LeaderboardModel, SessionModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login




@login_required
def exam_session (request,sessionuuid) :
    
    session = get_object_or_404(SessionModel,uuid=sessionuuid)
    points = LeaderboardModel.objects.get(user=request.user)
    context = {}

    context['choices'] = session.answers.split('@')
    context['question'] = session.question
    context['audio'] = session.audio

    context['s'] = session
    context['points'] = points.points

    if request.method == "POST" :
        user_answer = request.POST['user_answer']
        session.user_answer = user_answer
        session.save()

        if session.correct_answer == user_answer :
            points.points = points.points + 5
            points.save()
            context['points'] = points.points

 

    return render(request,'question.html',context)


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
        
    choices = '@'.join(all_choices)

    s = SessionModel.objects.create(

        user = request.user,
        question = text,
        uuid = f'{uuid.uuid4()}',
        answers = choices,
        correct_answer = surah.surah_name,
        audio = ayah.audio
    )

    return redirect('s',s.uuid)


@login_required
def profile (request)  :

    # top 10 leaders
    leaders = LeaderboardModel.objects.order_by('-points')[:10]
    points = LeaderboardModel.objects.get(user=request.user)

    return render(request,'profile.html',{'leaders':leaders,'points':points.points})


def login (request) : 

    context = {}

    if request.method == "POST" :
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email)
        if user :
            user = user.first()
            auth = authenticate(username = user.username,password = password)
            
            if auth is not None :
                auth_login(request,user)
                return redirect('profile')
            else :
                context['msg'] = 'كلمة مرور خاطئة'
            
        else :
            context['msg'] = 'البيانات غير صحيحة'


    return render(request,'login.html',context)


def register (request) : 

    if request.method == "POST" : 
        name = request.POST['name']
        username = f'{uuid.uuid4()}'
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

        return redirect('profile')


    return render(request,'register.html')

