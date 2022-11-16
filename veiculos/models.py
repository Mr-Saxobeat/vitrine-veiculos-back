from django.db import models

class Veiculo(models.Model):
    Marca = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=50)
    Valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['Valor']
