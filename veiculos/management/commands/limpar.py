from django.core.management.base import BaseCommand
from veiculos.models import Veiculo

class Command(BaseCommand):
    help = 'Limpa todos os veículos do banco de dados.'

    def handle(self, *args, **kwargs):
        Veiculo.objects.all().delete()