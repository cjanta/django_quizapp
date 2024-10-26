# Poll mit Django Tutorial

- https://docs.djangoproject.com/en/5.1/intro/tutorial01/
- python Installation erforderlich
- OS Pfadvariable einrichten um nicht immer den ganzen Pfad in der Shell eingeben zu müssen

# Vorbereitung/Setup des Repositories

## GitHub
- github projekt anlegen und lokal herunter clonen  
- **.gitignore** file erstellen und folgende Zeile hinzufügen: **.venv/**  
damit der Inhalt der virtuellen Umgebung **NICHT** mit github-repo abgeglichen wird.

## Virtuelle Umgebung (.venv) erstellen und aktivieren
python -m venv .venv

.venv/scripts/activate

## Django auf der virtuellen Umgebung (.venv) installieren

pip install django

*Überprüfung von django*  

python -m django --version

## Django Projekt erstellen Name=quiz_project

- in den Ordner wechseln in dem das Django Projekt erstellt werden soll
- **django-admin startproject quiz_project  **
````
Note

You’ll need to avoid naming projects after built-in Python or Django components.   
In particular, this means you should avoid using names like django (which will conflict with Django itself)   
or test (which conflicts with a built-in Python package).

````

## TEST: lokalen Django Server zum Test starten auf Port:8000

- cd quiz_project
- optional django updaten mit: python manage.py migrate
- python manage.py runserver
- http://127.0.0.1:8000/
- server stoppen im Terminal: **Strg+c**
````
Automatic reloading of runserver

The development server automatically reloads Python code for each request as needed.  
You don’t need to restart the server for code changes to take effect.   
However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.
````

# Tutorial umsetzen 


https://docs.djangoproject.com/en/5.1/intro/tutorial01/


## Erste Applikation zum Projekt erstellen
````
Projects vs. apps

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
````
- python manage.py startapp poll_app


## Erste View erstellen

````py 
# Durch den Shell-Aufruf erzeugte...
# django\poll_site\poll_app\views.py
#from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from datetime import datetime
import random

def ask_new_question(request):
    name = 'Ben Hanter'
    wochentag = datetime.now().strftime('%A')
    zahl = random.randint(1,100)
    return render(request, 'index.html', {'wochentag' : wochentag, 'name' : name, 'zahl' : zahl} )
````

## In der poll_app, file urls.py erstellen
- "\quiz_project\poll_site\poll_app\" File: "**urls.py**" 

````py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ask_new_question),
]
````
## \quiz_project\urls.py, globale url-Konfiguration der Website anpassen

Sollte danach im wesentlichen wie folgt ausssehen:

````py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('poll_app.urls')),
]
````

## TEST: Server starten und Website testen
- python manage.py runserver
- http://127.0.0.1:8000/


## Datenbank anlegen
"\quiz_project\poll_app\" File: **models.py**
````py
from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.choice_text
````

## Angelegte Datenbank modelle aktivieren
"\quiz_project\" File: **settings.py**
- Bei INSTALLED_APPS 'poll_app' hinzufügen
````py
INSTALLED_APPS = [
    'poll_app',
````
- in den Ordner von manage.py wechseln
- python manage.py makemigrations poll_app

Es sollten nun "Modell Migrationen" für Question und Choice angelegt worden sein
````
Migrations for 'poll_app':
  poll_app\migrations\0001_initial.py
    + Create model Question
    + Create model Choice
````

Migrationen ausführen
- python manage.py migrate

**TEST: Datenbank Table in db.sqlite3 überprüfen.** 
- poll_app_choice
- poll_app_question

## Hinzufügen von Datensätzen
- TODO: Migration von einer csv
- interaktive shell: python manage.py shell
- oder mit der Django Admin Seite

## Django Admin
- python manage.py createsuperuser
- nache dem anlegen des superusers
- python manage.py runserver

## poll_app in der admin seite registrieren
"\quiz_project\" File **admin.py**
````py
from django.contrib import admin

from .models import Question

admin.site.register(Question)

````

Nun ist poll_app verbunden und es können die Registrierten Modelle bearbeitet werden  
also, Datensätze können hinzugefügt oder geändert werden werden.


## TODO: Views ausarbeiten, aus Datenbank zur Ansicht und von der Ansicht in die Datenbank
- https://docs.djangoproject.com/en/5.1/intro/tutorial03/