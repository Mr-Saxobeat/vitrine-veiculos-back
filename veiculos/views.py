from veiculos.models import Veiculo
from veiculos.serializers import VeiculoSerializer
from rest_framework import generics


class VeiculoList(generics.ListCreateAPIView):
    """
    Lista todos veículos ou cria um novo.
    """
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class VeiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Recupera, atualiza ou deleta um veículo.
    """
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer