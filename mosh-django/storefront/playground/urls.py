# TODO: HERE we have the controllers which map to the service aka Views.py
# TODO: EVERYTHING MUST BE IMPORTED IN THE URLS MODULE OF PARENT
from django.urls import path
# . = ./
from . import views


# TODO: DJANGO LOOK SPECIFICALLY FOR THIS "urlpatterns"
# URLConf
# FIXME: HAS TO BE A FREAKING URLPATTERNS
urlpatterns = [
    path('hello/', views.say_hello)
]