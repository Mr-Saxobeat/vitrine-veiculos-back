# Generated by Django 4.1.3 on 2022-11-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0002_remove_veiculo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='Valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
