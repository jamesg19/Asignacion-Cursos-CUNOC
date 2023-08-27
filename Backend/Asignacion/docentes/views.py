from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Docentes
from .serializer import DocenteSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class DocentesList(generics.ListCreateAPIView):
    queryset = Docentes.objects.all()
    serializer_class = DocenteSerializer


class DocentesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docentes.objects.all()
    serializer_class = DocenteSerializer


class DocenteDeleteById(generics.DestroyAPIView):
    queryset = Docentes.objects.all()
    serializer_class = DocenteSerializer


@csrf_exempt
def guardar_lista_objetos(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Itera sobre la lista de objetos y realiza la lógica de guardado en la base de datos
            for item in data:
                if Docentes.objects.filter(id=item['id']).exists():
                    return JsonResponse({'error': 'Docente con el mismo id ya existe ', 'detalle': str(item['id'])}, status = 409)
                else:
                    nuevo_objeto = Docentes(id=item['id'], nombre=item['nombre'], apellido=item['apellido'],
                                            horario_entrada=item['horario_entrada'],
                                            horario_salida=item['horario_salida'])
                    nuevo_objeto.save()

            return JsonResponse({'mensaje': 'Lista de objetos guardada correctamente'})

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Peticion mal compuesta', 'detalle': str(e)}, status=400)

        except Exception as e:
            return JsonResponse({'error': 'Error en el servidor', 'detalle': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
