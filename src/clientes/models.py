from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name="país"
        verbose_name_plural = "paises"
    


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais_origen = models.ForeignKey(Pais, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.apellido.capitalize()}, {self.nombre.upper()}"
    
    class Meta:
        verbose_name="cliente"
        verbose_name_plural = "clientes"





