from django.urls import path, include

from . import views

app_name = 'lobosevents'

urlpatterns = [

    path('event_registration/', views.event_registration, name='event_registration'),
    path('profile/', views.profile, name='profile'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
]
