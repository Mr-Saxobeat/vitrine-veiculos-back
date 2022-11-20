# Vitrine de veículos back

Para o desenvolvimento deste projeto foram utilizados:

- Python 3.11.0
- Django 4.1.3
- pipenv 2022.11.11
- PostgreSQL 15.1.1

1. Para a máquina virtual, utilize a lib [pipenv](https://pypi.org/project/pipenv/):
    ````
    pip install pipenv
    ````

1. Com a biblioteca instalada, execute o seguinte comando na pasta do repositório para instalar a máquina virtual:
    ````
    pipenv install
    ````

1. Ative a máquina virtual:
    ````
    pipenv shell
    ````

1. Com todas as libs instaladas, crie o arquivo app/.env para escrever as configurações seguindo o exemplo:
    ````
    DEBUG=False
    ALLOWED_HOSTS=127.0.0.1
    SECRET_KEY=gere uma secret key em https://djecrety.ir/ e cole aqui -- MUDE APENAS ESTAS DUAS LINHAS
    DATABASE_URL=postgres://USUARIO:SENHA@HOST:PORTA/NOMEDOBANCO -- MUDE APENAS ESTAS DUAS LINHAS
    ````

1. Execute as migrations do django:
    ````
    python manage.py migrate
    ````

1. Para popular o banco de dados, execute o comando:
    ````
    python manage.py popular
    ````

1. Se quiser limpar o banco de dados de veiculos, execute:
    ````
    python manage.py limpar
    ````

1. Agora é só executar o servidor django:
    ````
    python manage.py runserver
    ````