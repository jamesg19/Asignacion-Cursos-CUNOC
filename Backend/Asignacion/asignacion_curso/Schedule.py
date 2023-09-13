import json, time
from django.db.models import Q
from django.core.serializers import serialize
from django.db.models import Count, F
from django.core import serializers
from .Objetos.CursoOBJ import CursoOBJ
from .Objetos.SalonesOBJ import SalonesOBJ
from .Objetos.DocenteOBJ import DocenteOBJ
from .models import AlumnosCursos, DocentesCursos, Docentes, Cursos, Salones, Periodos, Horarios, HorarioCursos, \
    CursosSalones


class Schedule:
    def __init__(self):
        pass

    def getSchedule(self,id):

        horario= Horarios.objects.filter(id=id)
        print(horario)

        return horario
