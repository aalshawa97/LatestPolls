import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django_project.models import Question
from django.shortcuts import get_object_or_404, render
from django_project.forms import CreatePollForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def homePageView(request):
    context = {}
    return render(request, 'home.html', context)


def aboutPageView(request):
    context = {}
    return render(request, 'about.html', context)


def createPageView(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = CreatePollForm()
    context = {'form': form}
    return render(request, 'create.html', context)


def create_question(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        if question_text:
            question = Question.objects.create(question_text=question_text)
            messages.success(request, 'Question created successfully.')
            return redirect('question_detail', question_id=question.id)
        else:
            messages.error(request, 'Question text is required.')
    return render(request, 'create.html')


def votePageView(request, poll_id):
    context = {}
    return render(request, 'vote.html', context)

def resultsPageView(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'results.html', context)
