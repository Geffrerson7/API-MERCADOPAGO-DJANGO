# API-MERCADOPAGO-DJANGO 

## Descripción
API hecha con Django Rest Framework para crear pago con la librería de mercadopago en python

## Respuesta en la consola
![api-django-mercado-pago](https://user-images.githubusercontent.com/61089189/226239748-e84c6473-2839-41e0-b152-7b416420b81a.png)

## Run Locally

Clonar el repositorio

```bash
  https://github.com/Geffrerson7/API-MERCADOPAGO-DJANGO.git
```

Ir al directorio al proyecto

```bash
  cd API-MERCADOPAGO-DJANGO
```

## Setup
Crear un entorno virtual y lo activamos:

```sh
$ python virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego realizamos las migraciones.
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
