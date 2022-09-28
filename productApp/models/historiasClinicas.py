import email
from enum import unique
from operator import truediv
from django.db import models
from .medico import Medico
from .historico import HistoriaClinica

class historiasClinicas(models.Model):
    cant_historiasClinicas = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, related_name='historiasClinicas', on_delete=models.CASCADE)
    id_historia = models.ForeignKey(HistoriaClinica, related_name='historiasClinicas', on_delete=models.CASCADE)
