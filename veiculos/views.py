from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from veiculos.models import Veiculo
from veiculos.serializers import VeiculoSerializer

@csrf_exempt
def veiculo_list(request):
    """
    Lista todos veículos ou cria um novo.
    """
    if request.method == 'GET':
        veiculos = Veiculo.objects.all()
        serializer = VeiculoSerializer(veiculos, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VeiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, stats=400)

def veiculo_detail(request, pk):
    """
    Recupera, atualiza ou deleta um veículo.
    """
    try:
        veiculo = Veiculo.objects.get(pk=pk)
    except Veiculo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VeiculoSerializer(veiculo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VeiculoSerializer(veiculo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        veiculo.delete()
        return HttpResponse(status=204)
