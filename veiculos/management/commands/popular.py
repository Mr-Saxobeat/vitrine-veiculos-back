from django.core.management.base import BaseCommand
from veiculos.serializers import VeiculoSerializer

class Command(BaseCommand):
	help = 'Popula o banco de dados com carros.'

	def handle(self, *args, **kwargs):
		serializer = VeiculoSerializer(data=[
			{
				"Marca": "Peugeot",
				"Modelo": "307 Feline/Griff/Premi. 2.0 Flex 5p Aut",
				"Valor": "1000.00"
			},
			{
				"Marca": "Hyundai",
				"Modelo": "Excel L",
				"Valor": "2000.00"
			},
			{
				"Marca": "Matra",
				"Modelo": "Pick-Up CD 4x2 Curto/Longo 2.5 TDI Dies.",
				"Valor": "3000.00"
			},
			{
				"Marca": "AM Gen",
				"Modelo": "Hummer Hard-Top 6.5 4x4 Diesel TB",
				"Valor": "4000.00"
			},
			{
				"Marca": "Audi",
				"Modelo": "A4 2.4 V6 30V Quattro Tiptronic",
				"Valor": "5000.00"
			},
			{
				"Marca": "Ferrari",
				"Modelo": "F430 Spider F1",
				"Valor": "6000.00"
			},
			{
				"Marca": "VW - VolksWagen",
				"Modelo": "up! cross 1.0 T. Flex 12V 5p",
				"Valor": "7000.00"
			},
			{
				"Marca": "Envemo",
				"Modelo": "Camper 2.5/GL/GLS/Master 4.1",
				"Valor": "8000.00"
			},
			{
				"Marca": "Mitsubishi",
				"Modelo": "Pajero DAKAR 3.2 4x4 T.I. Dies. 5p Aut.",
				"Valor": "9000.00"
			},
			{
				"Marca": "Rover",
				"Modelo": "Mini Cooper 1.3",
				"Valor": "10000.00"
			},
			{
				"Marca": "Nissan",
				"Modelo": "Terrano II SLX 2.7 Diesel",
				"Valor": "11000.00"
			},
			{
				"Marca": "VW - VolksWagen",
				"Modelo": "VOYAGE Comfortline 1.0 T.Flex 12V 4p",
				"Valor": "12000.00"
			},
			{
				"Marca": "Hyundai",
				"Modelo": "Excel GS",
				"Valor": "13000.00"
			},
			{
				"Marca": "Engesa",
				"Modelo": "Engesa 4x4 2.5/4.1",
				"Valor": "14000.00"
			},
			{
				"Marca": "Daihatsu",
				"Modelo": "Cuore 0/TS0 85i",
				"Valor": "15000.00"
			},
			{
				"Marca": "Alfa Romeo",
				"Modelo": "155",
				"Valor": "16000.00"
			},
			{
				"Marca": "Suzuki",
				"Modelo": "Sidekick Canvas",
				"Valor": "17000.00"
			},
			{
				"Marca": "Lexus",
				"Modelo": "IS-250 2.5 24V 208cv Aut.",
				"Valor": "18000.00"
			},
			{
				"Marca": "Acura",
				"Modelo": "Integra GS 1.8",
				"Valor": "19000.00"
			},
			{
				"Marca": "Audi",
				"Modelo": "S8 4.2 Mec",
				"Valor": "20000.00"
			},
			{
				"Marca": "Rolls-Royce",
				"Modelo": "Phantom 6.7 V12 Aut.",
				"Valor": "21000.00"
			}
		],
		many=True
		)
		if (serializer.is_valid()):
			serializer.save()
		else:
			print(serializer.errors)
