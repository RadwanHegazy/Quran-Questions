from . import views
from django.urls import path


urlpatterns = [

    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),

    path('',views.profile,name='profile'),
    path('exam/',views.exam,name='exam'),

]