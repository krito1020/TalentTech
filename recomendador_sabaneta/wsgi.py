import os # libreria para manejar el sistema operativo
from django.core.wsgi import get_wsgi_application # importar la funcion get_wsgi_application de django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') # establecer la variable de entorno DJANGO_SETTINGS_MODULE con el valor 'settings'

application = get_wsgi_application() # crear la aplicacion WSGI llamando a la funcion get_wsgi_application