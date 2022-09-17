from django.contrib import admin
from .models.registroSignosVitales import SignosVitales
from .models.historico import HistoriaClinica
from .models.usuarios import Usuario
from .models.medico import Medico
from .models.paciente import Paciente
from .models.familiar import Familiar
from .models.enfermero import Enfermero
from .models.pacientesAsignados import pacientesAsignados
from .models.historiasClinicas import historiasClinicas

# Register your models here.
admin.site.register(Usuario)
admin.site.register(SignosVitales)
admin.site.register(HistoriaClinica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Enfermero)
admin.site.register(pacientesAsignados)
admin.site.register(historiasClinicas)