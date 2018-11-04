"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from questions.views import *
#from django.urls import  include

urlpatterns = [
	url(r'about/', AboutView.as_view(), name='about'),
	url(r'ask/', AskView.as_view(), name='ask'),
	url(r'question/', QuestionView.as_view(), name='question'),
	url(r'tag/', TagView.as_view(), name='tag'),
	url(r'settings/', SettingsView.as_view(), name='settings'),
	url(r'login/', LoginView.as_view(), name='login'),
	url(r'registration/', RegistrationView.as_view(), name='registration'),
    url(r'^admin/', admin.site.urls),
]
