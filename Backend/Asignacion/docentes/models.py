from django.db import models

# Create your models here.
''''-- Tabla Docentes
CREATE TABLE docentes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    horario_entrada TIME,
    horario_salida TIME
) ENGINE=InnoDB;'''


class Docentes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    horario_entrada = models.TimeField(blank=True, null=True)
    horario_salida = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docentes'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"