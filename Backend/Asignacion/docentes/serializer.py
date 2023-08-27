from rest_framework import serializers
from .models import Docentes


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docentes
        fields = '__all__'
