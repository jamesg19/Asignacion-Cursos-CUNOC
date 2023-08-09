-- Crear la base de datos
DROP SCHEMA IF EXISTS `CUNOC`;

CREATE SCHEMA `CUNOC`;

-- Usar la base de datos
USE CUNOC;

-- Tabla Docentes
CREATE TABLE docentes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    horario_entrada TIME,
    horario_salida TIME
) ENGINE=InnoDB;

-- Tabla Alumnos
CREATE TABLE alumnos (
    carnet INT PRIMARY KEY,
    nombres VARCHAR(50),
    apellidos VARCHAR(50)
) ENGINE=InnoDB;

-- Tabla Mobiliario
CREATE TABLE mobiliario (
    id INT PRIMARY KEY,
    nombre VARCHAR(50)
) ENGINE=InnoDB;

-- Tabla Salones
CREATE TABLE salones (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    capacidad INT,
    tipo_mobiliario INT,
    disponible BOOLEAN,
    FOREIGN KEY (tipo_mobiliario) REFERENCES mobiliario(id)
) ENGINE=InnoDB;

-- Tabla Carreras
CREATE TABLE carreras (
    id INT PRIMARY KEY,
    nombre VARCHAR(100)
) ENGINE=InnoDB;

-- Tabla Cursos
CREATE TABLE cursos (
    id_curso INT ,
    id_carrera INT,
    nombre_curso VARCHAR(100),
    duracion_periodo INT,
    numero_semestre INT,
    PRIMARY KEY (id_curso, id_carrera)
) ENGINE=InnoDB;

-- Tabla Docentes_Cursos (relación muchos a muchos)
-- DOCENTES APTOS PARA IMPARTIR UN CURSO
CREATE TABLE docentes_cursos (
    docente_id INT,
    curso_id INT,
    PRIMARY KEY (docente_id, curso_id),
    FOREIGN KEY (docente_id) REFERENCES docentes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
) ENGINE=InnoDB;

-- ASIGNACIONES
-- Tabla Periodos de cursos
CREATE TABLE periodos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    hora_inicio TIME,
    hora_fin TIME
) ENGINE=InnoDB;

-- Tabla HorarioCursos
CREATE TABLE horario_cursos (
    id INT PRIMARY KEY NOT NULL,
    curso_id INT NOT NULL,
    docente_id INT NOT NULL,
    salon_id INT NOT NULL,
    seccion VARCHAR(5) NOT NULL,
    dias_semana VARCHAR(50),
    periodo_inicio INT NOT NULL,
    periodo_fin INT NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (docente_id) REFERENCES docentes(id),
    FOREIGN KEY (salon_id) REFERENCES salones(id),
    FOREIGN KEY (periodo_inicio) REFERENCES periodos(id)
    FOREIGN KEY (periodo_fin) REFERENCES periodos(id)
);

-- (PRE-ASIGNACIONES)
-- Tabla Alumnos_Cursos (relación muchos a muchos con atributos extras)
CREATE TABLE alumnos_cursos (
    alumno_carnet INT,
    curso_id INT,
    semestre INT,
    ciclo INT,
    PRIMARY KEY (alumno_carnet, curso_id),
    FOREIGN KEY (alumno_carnet) REFERENCES alumnos(carnet),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
) ENGINE=InnoDB;
