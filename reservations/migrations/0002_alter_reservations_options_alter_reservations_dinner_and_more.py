# Generated by Django 4.1 on 2023-02-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservations',
            options={'verbose_name': 'Reservacion', 'verbose_name_plural': 'Reservaciones'},
        ),
        migrations.AlterField(
            model_name='reservations',
            name='dinner',
            field=models.IntegerField(verbose_name='comensales'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='reservation_date',
            field=models.DateField(verbose_name='fecha de reserva'),
        ),
    ]
