# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse, Http404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from questions.models import *
# Create your views here.

def paginate(objects_list, request, amount):
    pag = Paginator(objects_list, amount)
    asd = request.GET.get('page')
    try:
        page = pag.page(asd)
    except PageNotAnInteger:
        page = pag.page(1)
    except EmptyPage:
        page = pag.page(pag.num_pages)
    return page

'''def paginate(objects, request, amount):
    paginator = Paginator(objects, amount)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page'''

def index(request):
    latest_question_list = Question.objects.order_by()
    template = loader.get_template('bender.html')
    context = {
    'questions': paginate(latest_question_list, request, 2)
    }
    return HttpResponse(template.render(context, request))
'''
def index(request):
    return render(request, 'bander.html', {
        'questions': paginate(request, Question.objects.all(), 3),
        })'''

def question(request, number):
    question = get_object_or_404(Question, pk=number)
    # latest_question_list = Question.objects.get
    return render(request,'questions.html', context={
        'questionOne':question,
        'questions' :question.answers.all()
        })
   
def ask(request):
    latest_question_list = Question.objects.order_by()
    template = loader.get_template('ask.html')
    context = {
        'questions': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def settings(request):
    latest_question_list = Question.objects.order_by()
    template = loader.get_template('settings.html')
    context = {
        'questions': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    latest_question_list = Question.objects.order_by()
    template = loader.get_template('login.html')
    context = {
        'questions': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def registration(request):
    latest_question_list = Question.objects.order_by()
    template = loader.get_template('registration.html')
    context = {
        'questions': latest_question_list,
    }
    return HttpResponse(template.render(context, request))




def tag(request):
    latest_question_list = Question.objects.order_by()
    template = loader.get_template('tag.html')
    context = {
        'questions': paginate(latest_question_list, request, 2)
    }
    return HttpResponse(template.render(context, request))

def hot(request):
    latest_question_list = Question.objects.top()
    template = loader.get_template('hot.html')
    context = {
        'questions': paginate(latest_question_list, request, 3)
    }
    return HttpResponse(template.render(context, request))