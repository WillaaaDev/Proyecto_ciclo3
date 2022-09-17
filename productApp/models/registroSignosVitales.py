from operator import truediv
from django.db import models

class SignosVitales(models.Model):
    id_registro = models.AutoField(primary_key=True)
    oximetria = models.CharField('oximetria', max_length = 100)
    frecuencia_respiratoria = models.CharField('frecuencia_respiratoria', max_length = 100)
    frecuencia_cardiaca = models.CharField('frecuencia_cardiaca', max_length = 100)
    temperatura = models.CharField('temperatura', max_length = 100)
    precion_arterial = models.CharField('precion_arterial', max_length = 100)
    glicemias = models.CharField('glicemias', max_length = 100)
