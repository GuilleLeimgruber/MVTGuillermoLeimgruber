from django.db import models

# Create your models here.




class Menus(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'nombre del menu')
    price = models.FloatField(verbose_name= 'precio')
    stock = models.BooleanField(default=True, verbose_name= 'stock')
    image = models.ImageField(upload_to='menus', verbose_name= 'imagen')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

class Categories(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'





