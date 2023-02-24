from django.db import models

# Create your models here.




class Deliveries(models.Model):

    CHOICES = (
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'), 
        ('Transferencia', 'Transferencia'),
    )
        
    
    client = models.CharField(max_length=100, verbose_name= 'cliente')
    menu = models.CharField(max_length=100, verbose_name= 'menu')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha de creacion')
    payment_method = models.CharField(max_length=13, choices=CHOICES, verbose_name= 'metodo de pago')


    def __str__(self):
        return  f'{self.client} - {self.menu}'

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliverys'
