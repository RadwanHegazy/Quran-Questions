from django.db import models
from django.contrib.auth.models import User




class LeaderboardModel (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)




class Surah(models.Model) :
    surah_name = models.TextField()
    surah_type = models.TextField()
    number_of_ayahs = models.IntegerField()


class Ayah (models.Model):
    surah = models.ForeignKey(Surah,on_delete=models.CASCADE)
    text = models.TextField()
    number = models.IntegerField()
    audio = models.TextField(default='')
