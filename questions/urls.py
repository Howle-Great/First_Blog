from django.conf.urls import url, include
from django.contrib import admin
from questions.views import *
#from django.urls import  include

urlpatterns = [
	url(r'^$', index, name='about'),
    url(r'^ask', ask, name='ask'),
    url(r'^question/(?P<number>[0-9]+)/', question, name='question'),
    url(r'^tag/gintama', tag, name='tag'),   
    url(r'^login', login, name='login'),
    url(r'^signup', registration, name='signup'),
    url(r'^hot', hot, name='hot'),

    url(r'^settings', settings, name='settings'),
]