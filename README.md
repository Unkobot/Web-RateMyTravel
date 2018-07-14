# Web-RateMyTravel
# Primero:
- Django == 2.0.2
- mysqlcliente = 1.3.13
- Pillow = 5.2.0
- Django-ckeditor == 5.5.0
- lazy-object-proxy == 1.3.1

# Segundo:
## antes de ejecutar el servidor, ejecutar los siguientes comandos:
- python manage.py makemigrations newsfeed
- python manage.py makemigrations registration
## ya que estas dos Apps usan BD
- python manage.py migrate
- para generar las tablas