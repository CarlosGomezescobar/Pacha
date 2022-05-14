# Pacha
Pacha Admin/User
es un sistema operativo para llevar administracion del desarrollo web

Ubuntu: 20.04,
Backend: Python 3.8.10,
Frontend: HTML, CSS, Javascript,Bootstrap, Jquery
Django: 4.0,
BDD: sqlite3,
Control de Versiones: Git



Para iniciar debes crear un Entorno Virtual:


- Activar el Entorno Virtual:

	source myvenv/bin/activate
 
- Descargar las Dependencias para el projecto:
	pip3 install -r requirements.txt

Crear Proyecto: 
	- Crear Proyecto
		* django-admin startproject Pacha .
		
	- Crear App.
		 * python3 manage.py startapp core

Hacer Migraciones:
 1. python3 manage.py makemigrations
 2. python3 manage.py migrate
 3. python3 manage.py createsuperuser

Go...
python3 manage.py runserver
