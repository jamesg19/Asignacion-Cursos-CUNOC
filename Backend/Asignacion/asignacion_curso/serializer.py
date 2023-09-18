from rest_framework import serializers
from .models import AlumnosCursos, HorarioCursos, Periodos, Salones, DocentesCursos, Horarios


class AlumnosCursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnosCursos
        fields = '__all__'

class HorarioCursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioCursos
        fields = '__all__'
        depth = 1
class PeriodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodos
        fields = '__all__'
        depth = 2

class SalonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salones
        fields = '__all__'
        depth = 1

class HorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horarios
        fields = '__all__'
        depth = 3

class DocentesCursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocentesCursos
        fields = '__all__'
        depth = 3