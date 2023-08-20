from django.contrib import admin
from .models import Surah, Ayah, LeaderboardModel
from django.contrib.auth.models import Group


class LeaderBoardPanel (admin.ModelAdmin) : 
    list_display = ['user','points']
    ordering = ['-points']

class SurahPanel (admin.ModelAdmin)  :
    list_display = ['surah_name','surah_type']

class AyahPanel (admin.ModelAdmin) : 
    list_display = ['surah','number']

admin.site.register(Surah, SurahPanel)
admin.site.register(Ayah,AyahPanel)
admin.site.register(LeaderboardModel, LeaderBoardPanel)


admin.site.unregister(Group)