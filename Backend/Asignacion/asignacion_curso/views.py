
from django.shortcuts import render
from django.views import View
from requests import request

# Create your views here.
from django.core import serializers

from rest_framework import generics
from .models import AlumnosCursos
from .arbol_decision import ArbolDecision
from .serializer import AlumnosCursosSerializer
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
        data = arbol.cursos_preasignados()


        # Crea una respuesta JSON
        return JsonResponse({'mensaje': data})
