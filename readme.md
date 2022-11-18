# Vitrine de veículos back

Para o desenvolvimento deste projeto foram utilizados:

- Python 3.11.0
- pipenv version 2022.11.11
- asgiref 3.5.2
- Django 4.1.3
- django-cors-headers 3.13.0
- djangorestframework 3.14.0
- djangorestframework-simplejwt 5.2.2
- PyJWT 2.6.0
- pytz 2022.6
- sqlparse 0.4.3
- tzdata 2022.6

1. Para a máquina virtual, utilize a lib [pipenv](https://pypi.org/project/pipenv/):
    ````
    pip install pipenv
    ````

1. Com a biblioteca instalada, instale a máquina virtual do repositório:
    ````
    pipenv install
    ````

1. Ative a máquina virtual:
    ````
    pipenv shell
    ````

1. Execute as migrations do django:
    ````
    python manage.py migrate
    ````

1. Agora é só executar o servidor django:
    ````
    python manage.py runserver
    ````