from django.db import models

class Veiculo(models.Model):
    Nome = models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=50)
    Valor = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['Valor']
