import email
from enum import unique
from operator import truediv
from django.db import models
from .medico import Medico
from .paciente import Paciente

class pacientesAsignados(models.Model):
    cant_pacientes = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, related_name='medico', on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, related_name='medico', on_delete=models.CASCADE)