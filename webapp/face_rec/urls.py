from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # display both cameras
    path('', views.index, name='index'),

    # access the laptop camera
    path('video_feed', views.video_feed, name='video_feed'),

    # access the phone camera
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),

]
