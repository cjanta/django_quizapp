from django.shortcuts import render
from .models import Question
from datetime import datetime
import random

def ask_new_question(request):
    name = 'Ben Hanter'
    wochentag = datetime.now().strftime('%A')
    zahl = random.randint(1,100)
    #all_questions = Question.objects.all()
    all_questions = Question.objects.prefetch_related('answers')
    question = all_questions[random.randint(1,len(all_questions)-1)]
    return render(request, 'index.html', {'wochentag' : wochentag, 'name' : name, 'zahl' : zahl , 'question' : question })
