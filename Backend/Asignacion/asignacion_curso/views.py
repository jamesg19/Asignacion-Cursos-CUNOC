import self as self
from django.shortcuts import render
from django.views import View
from requests import request

# Create your views here.
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework import generics
from .models import AlumnosCursos, HorarioCursos, Periodos, Salones
from .arbol_decision import ArbolDecision
from .Schedule import Schedule

from .serializer import AlumnosCursosSerializer, HorarioCursosSerializer, PeriodosSerializer, SalonesSerializer
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
        #data = arbol.cursos_preasignados()
        data=arbol.simular()

        # Crea una respuesta JSON
        return JsonResponse({'mensaje': data})
        #return JsonResponse({data})




class HorariosCursos(generics.ListCreateAPIView):
    serializer_class = HorarioCursosSerializer
    def get_queryset(self):
        print("Entra en horario")
        horario_id=self.kwargs.get('horario_id')
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
        queryset = Salones.objects.filter(edificio_id=edificio_id,disponible=1)
        print(queryset)
        return queryset


