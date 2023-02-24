from django.db import models

# Create your models here.




class Reservations(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'nombre')
    dinner = models.IntegerField(verbose_name= 'comensales')
    reservation_date = models.DateField(verbose_name= 'fecha de reserva')
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Reservacion'
        verbose_name_plural = 'Reservaciones'