from rest_framework import serializers
from .models import AlumnosCursos, HorarioCursos, Periodos, Salones


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
        depth = 1

class SalonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salones
        fields = '__all__'
        depth = 1