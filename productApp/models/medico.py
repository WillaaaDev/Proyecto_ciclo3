import email
from enum import unique
from operator import truediv
from django.db import models
from .usuarios import Usuario

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    Nombre = models.CharField('Nombre', max_length = 100)
    Especialidad = models.CharField('Especialidad', max_length = 100)
    Telefono = models.CharField('Telefono', max_length = 100)
    usuario_id = models.ForeignKey(Usuario, related_name='id_usuario', on_delete=models.CASCADE)
