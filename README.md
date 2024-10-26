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

## lokalen Django Server starten auf Port:8000

- cd django/poll_site
- optional django updaten mit: python manage.py migrate
- python manage.py runserver
- http://127.0.0.1:8000/
- server stoppen im Terminal: **Strg+c**

# Tutorial umsetzen 
https://docs.djangoproject.com/en/5.1/intro/tutorial01/



