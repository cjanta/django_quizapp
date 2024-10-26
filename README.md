# Poll Tutorial

https://docs.djangoproject.com/en/5.1/intro/tutorial01/

- python installation erforderlich
- OS Pfandvariable einrichten um nicht immer den ganzen Pfad in der Shell eingeben zu müssen

# Vorbereitung/Setup des Repositories

## GitHub
- github projekt anlegen und lokal herunter clonen  
- **.gitignore** file erstellen und folgende Zeile hinzufügen: **.venv/**  
damit der Inhalt der virtuellen Umgebung **NICHT** mit github-repo abgeglichen wird.

## Virtuelle Umgebung (.venv) erstellen und aktivieren
python -m venv .venv

.venv\Scripts\activate

## Django auf der virtuellen Umgebung (.venv) installieren

pip install django

Überprüfung von django  
python -m django --version

## Django Projekt erstellen Name=poll_site

- in den Ordner wechseln in dem das Django Projekt erstellt werden soll
- Unterordner **django** erstellen (nicht zwingend allerdings von mir gewünscht)
- cd django
- django-admin startproject poll_site  
````
Note

You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like django (which will conflict with Django itself) or test (which conflicts with a built-in Python package).

````

## TEST: lokalen Django Server zum Test starten auf Port:8000

- cd django/poll_site
- optional django updaten mit: python manage.py migrate
- python manage.py runserver
- http://127.0.0.1:8000/
- server stoppen im Terminal: **Strg+c**
````
Automatic reloading of runserver

The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.
````

# Tutorial umsetzen 


https://docs.djangoproject.com/en/5.1/intro/tutorial01/


## Erste Applikation zum Projekt erstellen
````
Projects vs. apps

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
````
- shell: python manage.py startapp poll_app


## Erste View erstellen

````py 
# Durch den Shell-Aufruf erzeugte...
# django\poll_site\poll_app\views.py
#from django.shortcuts import render
from django.http import HttpResponse

def hello_world():
    return HttpResponse("Anwort der View")
````

## In der poll_app, file urls.py erstellen
- "django\poll_site\poll_app\" File: "**urls.py**" 

````py
from django.urls import path

from . import views

urlpatterns = [
   path('', views.hello_world),
]
````
## django\poll_site\urls.py, globale url-Konfiguration der Website anpassen

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
- shell: python manage.py runserver
- http://127.0.0.1:8000/