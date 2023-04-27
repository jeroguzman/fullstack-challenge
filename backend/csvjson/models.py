from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']