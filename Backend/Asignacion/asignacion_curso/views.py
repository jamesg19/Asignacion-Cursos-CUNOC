import self as self
from django.shortcuts import render
from django.views import View
from requests import request

# Create your views here.
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from .models import AlumnosCursos, HorarioCursos, Periodos, Salones, Horarios
from .arbol_decision import ArbolDecision
from .Schedule import Schedule

from .serializer import AlumnosCursosSerializer, HorarioCursosSerializer, PeriodosSerializer, SalonesSerializer, \
    HorariosSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

import json


# Create your views here.
@csrf_exempt
def SimularHorario(request):
    if request.method == 'GET':
        print("entra")
        arbol = ArbolDecision()
        data = arbol.simular()

        # Crea una respuesta JSON
        return JsonResponse({'mensaje': data})
        # return JsonResponse({data})

    if request.method == 'POST':
        # Obtener parametros
        try:
            objeto_python = json.loads(request.body)
            #objeto_python = json.loads(data)
            horario=Horarios
            horario.nombre=objeto_python["nombre"]
            horario.semestre = objeto_python["semestre"]
            horario.ciclo = objeto_python["ciclo"]
            horario.cantidad_minima = objeto_python["cantidad_minima"]
            horario.edificio_id = objeto_python["edificio_id"]
            horario.prioridad_semestre_ascendente = objeto_python["prioridad_semestre_ascendente"]
            horario.prioridad_semestre_descendente = objeto_python["prioridad_semestre_descendente"]
            horario.prioridad_demanda = objeto_python["prioridad_demanda"]
            horario.prioridad_semestre_actual = objeto_python["prioridad_semestre_actual"]
            horario.elegirSalonExclusivo = objeto_python["elegirSalonExclusivo"]
            horario.docente_horariolaboral = objeto_python["docente_horariolaboral"]

            arbol = ArbolDecision()
            data = arbol.simular(horario)

            return JsonResponse({'id': data})

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Peticion mal compuesta', 'detalle': str(e)}, status=400)


class HorariosCursos(generics.ListCreateAPIView):
    serializer_class = HorarioCursosSerializer

    def get_queryset(self):
        print("Entra en horario")
        horario_id = self.kwargs.get('horario_id')
        queryset = HorarioCursos.objects.filter(horario_id=horario_id).order_by('periodo_inicio__id')
        return queryset


class PeriodosEdificio(generics.ListCreateAPIView):
    serializer_class = PeriodosSerializer

    def get_queryset(self):
        print("ENTRA EN PERIODOS...")

        edificio_id = self.kwargs.get('edificio_id')
        print(edificio_id)
        queryset = Periodos.objects.filter(edificio_id=edificio_id)
        return queryset


class SalonesEdificio(generics.ListCreateAPIView):
    serializer_class = SalonesSerializer

    def get_queryset(self):
        print("ENTRA EN Salones...")
        edificio_id = self.kwargs.get('edificio_id')
        print(edificio_id)
        queryset = Salones.objects.filter(edificio_id=edificio_id, disponible=1)
        print(queryset)
        return queryset


class HorariosParametros(generics.ListCreateAPIView):
    serializer_class = HorariosSerializer

    def get_queryset(self):
        print("ENTRA EN parametros...")
        horario_id = self.kwargs.get('horario_id')
        print(horario_id)
        queryset = Horarios.objects.filter(id=horario_id)
        print(queryset)
        return queryset
