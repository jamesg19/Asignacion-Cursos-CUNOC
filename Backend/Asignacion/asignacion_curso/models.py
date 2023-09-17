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
    carrera = models.OneToOneField('Carreras', models.DO_NOTHING, primary_key=True)  # The composite primary key (carrera_id, curso_id) found, that is not supported. The first column is selected.
    curso = models.ForeignKey('Cursos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carrera_cursos'
        unique_together = (('carrera', 'curso'),)



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


class CursosSalones(models.Model):
    salon = models.OneToOneField('Salones', models.DO_NOTHING, primary_key=True)  # The composite primary key (salon_id, curso_id) found, that is not supported. The first column is selected.
    curso = models.ForeignKey(Cursos, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cursos_salones'
        unique_together = (('salon', 'curso'),)


class Docentes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    horario_entrada = models.TimeField(blank=True, null=True)
    horario_salida = models.TimeField(blank=True, null=True)
    periodo_inicio = models.ForeignKey('Periodos', models.DO_NOTHING, db_column='periodo_inicio', blank=True, null=True)
    periodo_fin = models.ForeignKey('Periodos', models.DO_NOTHING, db_column='periodo_fin',
                                    related_name='docentes_periodo_fin_set', blank=True, null=True)

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
    horario = models.ForeignKey('Horarios', models.DO_NOTHING)
    curso = models.ForeignKey(Cursos, models.DO_NOTHING)
    docente = models.ForeignKey(Docentes, models.DO_NOTHING, blank=True, null=True)
    salon = models.ForeignKey('Salones', models.DO_NOTHING)
    seccion = models.CharField(max_length=5)
    dias_semana = models.CharField(max_length=50, blank=True, null=True)
    periodo_inicio = models.ForeignKey('Periodos', models.DO_NOTHING, db_column='periodo_inicio')
    periodo_fin = models.ForeignKey('Periodos', models.DO_NOTHING, db_column='periodo_fin', related_name='horariocursos_periodo_fin_set')
    carrera = models.ForeignKey(Carreras, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'horario_cursos'


class Horarios(models.Model):
    nombre = models.CharField(max_length=50)
    semestre = models.IntegerField()
    ciclo = models.IntegerField()
    cantidad_minima = models.IntegerField()
    edificio_id = models.IntegerField()
    prioridad_semestre_ascendente = models.IntegerField(blank=True, null=True)
    prioridad_semestre_descendente = models.IntegerField(blank=True, null=True)
    prioridad_demanda = models.IntegerField(blank=True, null=True)
    prioridad_semestre_actual = models.IntegerField(blank=True, null=True)
    elegir_salon_exclusivo = models.IntegerField(blank=True, null=True)
    docente_horariolaboral = models.IntegerField(blank=True, null=True)

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
    edificio = models.ForeignKey(Edificio, models.DO_NOTHING)

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
