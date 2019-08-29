from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('allrooms', api.allrooms),
    url('say', api.say),
]
