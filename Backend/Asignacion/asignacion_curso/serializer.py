from rest_framework import serializers
from .models import AlumnosCursos


class AlumnosCursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnosCursos
        fields = '__all__'
