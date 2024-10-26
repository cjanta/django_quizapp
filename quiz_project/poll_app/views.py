from django.shortcuts import render
from .models import Question
from datetime import datetime
import random

def ask_new_question(request):
    name = 'Ben Hanter'
    wochentag = datetime.now().strftime('%A')
    zahl = random.randint(1,100)
    all_questions = Question.objects.all()
    q_text = all_questions[random.randint(1,len(all_questions)-1)]
    return render(request, 'index.html', {'wochentag' : wochentag, 'name' : name, 'zahl' : zahl , 'question' : q_text })
