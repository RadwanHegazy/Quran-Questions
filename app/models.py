from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class LeaderboardModel (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self) :
        return f'{self.user.username}'


class Surah(models.Model) :
    surah_name = models.TextField()
    surah_type = models.TextField()
    number_of_ayahs = models.IntegerField()

    def __str__(self) : 
        return f'{self.surah_name}'


class Ayah (models.Model):
    surah = models.ForeignKey(Surah,on_delete=models.CASCADE)
    text = models.TextField()
    number = models.IntegerField()
    audio = models.TextField(default='')


class SessionModel (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10000)

    answers = models.CharField(max_length=1000,default='')

    correct_answer = models.CharField(max_length=1000)
    user_answer = models.CharField(max_length=1000,default='')
    audio = models.URLField(default='')



@receiver(post_save, sender=User)
def CreateLieaderBoardModel (created,instance,**args) : 
    if created :
        LeaderboardModel.objects.create(user = instance)
