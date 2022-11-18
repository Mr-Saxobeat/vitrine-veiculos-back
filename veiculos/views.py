from veiculos.models import Veiculo
from veiculos.serializers import VeiculoSerializer
from rest_framework import viewsets
from rest_framework import permissions


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()