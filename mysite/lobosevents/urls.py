from django.urls import path, include

from . import views

app_name = 'lobosevents'

urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login_register/', views.login_register, name='login_register'),
    path('login/', views.login, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('event_registration/', views.event_registration, name='event_registration'),
    path('cancelorder/', views.cancelorder, name='cancelorder'),
    path('eventconfir/', views.event_reg_confirmation, name='event_reg_confirmation'),
    path('login/', views.login, name='login'),

]
