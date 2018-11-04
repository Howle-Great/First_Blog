# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

# Create your views here.


class AboutView(TemplateView):
	template_name = "base.html"

class AskView(TemplateView):
	template_name = "bender.html"

class QuestionView(TemplateView):
	template_name = "questions.html"

class TagView(TemplateView):
	template_name = "ask.html"

class SettingsView(TemplateView):
	template_name = "settings.html"

class RegistrationView(TemplateView):
	template_name = "registration.html"

class LoginView(TemplateView):
	template_name = "login.html"
		


def question_view(request, page = 1):
	questions = []
	for i in xrange(1,30):
		questions.append({
			'title': 'title' + str(i),
    		'id': i,
    		'text': 'text' + str(i),
    		'rating': 100 + i,
    		'link': 'answer',
    		'avatar': 'empty.png'
			})
	paginator = Paginator(questions, 10);

	try:
		questions_page = paginator.page(page)
	except EmptyPage:
		raise Http404
	return render(request, 'hot.html', {
		'questions': questions_page,
		'pages': range(1, paginator.num_pages + 1)
		})