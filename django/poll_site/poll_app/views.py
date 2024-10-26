from django.shortcuts import render
from datetime import datetime
import random
from django.http import HttpResponse

def hello_world(request):
    name = 'Ben Hanter'
    wochentag = datetime.now().strftime('%A')
    zahl = random.randint(1,100)
    return HttpResponse("Antwort der View")
    # return render(request, 'index.html', {'wochentag' : wochentag, 'name' : name, 'zahl' : zahl} )