from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),

    path('',views.profile,name='profile'),
    path('exam/',views.exam,name='exam'),
    path('exam/session/<str:sessionuuid>/',views.exam_session,name='s'),


    path('logout/',LogoutView.as_view(),name='logout')

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
