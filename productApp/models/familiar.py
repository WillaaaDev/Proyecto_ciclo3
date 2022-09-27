import email
from enum import unique
from operator import truediv
from django.db import models
from .usuarios import Usuario
from .historico import HistoriaClinica
from .paciente import Paciente

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    Nombre = models.CharField('Nombre', max_length = 100)
    Apellido = models.CharField('Especialidad', max_length = 100)
    Cedula = models.CharField('Especialidad', max_length = 100)
    Celular = models.CharField('Especialidad', max_length = 100)
    Direccion = models.CharField('Especialidad', max_length = 100)
    paciente_id = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE) 
    historia_id = models.ForeignKey(HistoriaClinica, related_name='historiasClinicas', on_delete=models.CASCADE) 
    usuario_id = models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE)
