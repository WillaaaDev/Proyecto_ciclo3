import email
from enum import unique
from operator import truediv
from django.db import models
from .usuarios import Usuario
from .paciente import Paciente

class Enfermero(models.Model):
    id_enfermero = models.AutoField(primary_key=True)
    Nombre = models.CharField('Nombre', max_length = 100)
    Apellido = models.CharField('Apellido', max_length = 100)
    Celular = models.CharField('Celular', max_length = 100)
    paciente_id = models.ForeignKey(Paciente, related_name='enfermero', on_delete=models.CASCADE) 
    usuario_id = models.ForeignKey(Usuario, related_name='enfermero', on_delete=models.CASCADE)
