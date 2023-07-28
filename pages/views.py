import os
import django

from django_project import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django_project.models import Question, Answer
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
    question = Question.objects.get(pk=poll_id)
    if Answer.question == question:
        answer = Answer.answer_text# where ansID = poll_id
    try:
        selected_choice = answer
    except(KeyError, Answer.DoesNotExist):
        print('Error')
        #Handle invalid choices
        return render(request, 'polls/detail.html')
    else:
        selected_choice.vote += 1
        selected_choice.save()
    context = {}
    return redirect('results', question_id = poll_id)
    #return render(request, 'vote.html', context)

def resultsPageView(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    #Fix
    #total_votes = choices
    # Retrieve the choices associated with the question
    #choice_text = models.CharField(max_length = 100)
    #context = {'question': question, 'choices': choices}
    # Retrieve the total votes for the question
    #total_votes = question.total()

    #context = {'question': question, 'total_votes': total_votes}
    return render(request, 'results.html', context)
    #return render(request, 'results.html', context)
