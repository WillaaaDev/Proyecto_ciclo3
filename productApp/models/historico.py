from operator import truediv
from django.db import models
from .registroSignosVitales import SignosVitales

class HistoriaClinica(models.Model):
    id_historia = models.AutoField(primary_key=True)
    signos_vitales = models.ForeignKey(SignosVitales, related_name='signos_vitales', on_delete=models.CASCADE)
    resumen_historia_clinica = models.CharField('resumen_historia_clinica', max_length = 100)
    mecicamentos_terapidas = models.CharField('mecicamentos_terapidas', max_length = 100)
    diagnostico = models.CharField('diagnostico', max_length = 100)
    sugerencia_cuidado = models.CharField('sugerencia_cuidado', max_length = 100)