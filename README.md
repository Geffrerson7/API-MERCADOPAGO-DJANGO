# API-MERCADOPAGO-DJANGO 

## Descripción
API hecha con Django Rest Framework para crear pago con la librería de mercadopago en python

## Respuesta en la consola

![payment-response](https://user-images.githubusercontent.com/61089189/235060452-b6615b8f-9fc2-4757-afb7-2f3c48d9b744.png)

## Environment Variables

Crear las siguientes variables de entornno en el archivo .env

`YOUR_PUBLIC_KEY`

`YOUR_ACCESS_TOKEN`

## Run Locally

Clonar el repositorio

```bash
  https://github.com/Geffrerson7/API-MERCADOPAGO-DJANGO.git
```

Ir al directorio del proyecto

```bash
  cd API-MERCADOPAGO-DJANGO
```

## Setup
Crear un entorno virtual y activarlo:

```sh
$ virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego realizar las migraciones.
```sh
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la apliación
```sh
(env)$ python manage.py runserver
```

## Aplicación frontend de prueba
[Shopping Cart](https://github.com/Geffrerson7/SHOPPING-CART)

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
