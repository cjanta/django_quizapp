from django.shortcuts import render
from datetime import datetime
import random

def ask_new_question(request):
    name = 'Ben Hanter'
    wochentag = datetime.now().strftime('%A')
    zahl = random.randint(1,100)
    return render(request, 'index.html', {'wochentag' : wochentag, 'name' : name, 'zahl' : zahl} )
