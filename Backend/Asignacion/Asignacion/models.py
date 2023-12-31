# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumnos(models.Model):
    carnet = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'alumnos'


class AlumnosCursos(models.Model):
    alumno_carnet = models.OneToOneField(Alumnos, models.DO_NOTHING, db_column='alumno_carnet', primary_key=True)  # The composite primary key (alumno_carnet, curso_id, semestre, ciclo) found, that is not supported. The first column is selected.
    curso = models.ForeignKey('Cursos', models.DO_NOTHING)
    semestre = models.IntegerField()
    ciclo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumnos_cursos'
        unique_together = (('alumno_carnet', 'curso', 'semestre', 'ciclo'),)


class CarreraCursos(models.Model):
    carrera_id = models.IntegerField(primary_key=True)  # The composite primary key (carrera_id, curso_id) found, that is not supported. The first column is selected.
    curso_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carrera_cursos'
        unique_together = (('carrera_id', 'curso_id'),)


class CarreraEdificio(models.Model):
    carrera = models.OneToOneField('Carreras', models.DO_NOTHING, primary_key=True)  # The composite primary key (carrera_id, edificio_id) found, that is not supported. The first column is selected.
    edificio = models.ForeignKey('Edificio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carrera_edificio'
        unique_together = (('carrera', 'edificio'),)


class Carreras(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carreras'


class Cursos(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    nombre_curso = models.CharField(max_length=100, blank=True, null=True)
    duracion_periodo = models.IntegerField()
    numero_semestre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cursos'


class Docentes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    horario_entrada = models.TimeField(blank=True, null=True)
    horario_salida = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docentes'


class DocentesCursos(models.Model):
    docente = models.OneToOneField(Docentes, models.DO_NOTHING, primary_key=True)  # The composite primary key (docente_id, curso_id) found, that is not supported. The first column is selected.
    curso = models.ForeignKey(Cursos, models.DO_NOTHING)
    titular = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docentes_cursos'
        unique_together = (('docente', 'curso'),)


class Edificio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'edificio'


class HorarioCursos(models.Model):
    id = models.IntegerField(primary_key=True)
    horario = models.ForeignKey('Horarios', models.DO_NOTHING)
    curso = models.ForeignKey(Cursos, models.DO_NOTHING)
    docente = models.ForeignKey(Docentes, models.DO_NOTHING)
    salon = models.ForeignKey('Salones', models.DO_NOTHING)
    seccion = models.CharField(max_length=5)
    dias_semana = models.CharField(max_length=50, blank=True, null=True)
    periodo_inicio = models.ForeignKey('Periodos', models.DO_NOTHING, db_column='periodo_inicio')
    periodo_fin = models.ForeignKey('Periodos', models.DO_NOTHING, db_column='periodo_fin', related_name='horariocursos_periodo_fin_set')

    class Meta:
        managed = False
        db_table = 'horario_cursos'


class Horarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'horarios'


class Mobiliario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mobiliario'


class Periodos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        managed = False
        db_table = 'periodos'


class Salones(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    tipo_mobiliario = models.ForeignKey(Mobiliario, models.DO_NOTHING, db_column='tipo_mobiliario')
    edificio = models.ForeignKey(Edificio, models.DO_NOTHING)
    disponible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salones'
