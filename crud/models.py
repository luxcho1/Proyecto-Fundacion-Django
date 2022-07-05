from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering=['idCategoria']

    def __str__(self):
        return self.nombreCategoria

class Remedio(models.Model):
    idRemedio = models.CharField(primary_key=True, max_length=10, verbose_name='Id remedio')

    nombreRemedio = models.CharField(max_length=50, verbose_name='Nombre del remedio')
    
    descripcion = models.CharField(max_length=100, verbose_name='Descripción del remedio')

    precio = models.IntegerField(verbose_name='Precio')

    cantidad = models.IntegerField(verbose_name='cantidad')

    imagen = models.ImageField(verbose_name='Imagen',upload_to='Remedios',null=True,blank=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Remedio'
        verbose_name_plural='Remedios'
        ordering=['idRemedio']

    def __str__(self):
        return self.descripcion