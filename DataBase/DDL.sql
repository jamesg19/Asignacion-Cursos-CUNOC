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
    nombres VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Tabla Mobiliario
CREATE TABLE mobiliario (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Tabla Edificio
CREATE TABLE edificio (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Tabla Salones
CREATE TABLE salones (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    capacidad INT NOT NULL,
    tipo_mobiliario INT NOT NULL,
    edificio_id INT NOT NULL,
    disponible BOOLEAN NOT NULL,
    FOREIGN KEY (tipo_mobiliario) REFERENCES mobiliario(id),
    FOREIGN KEY (edificio_id) REFERENCES edificio(id)
) ENGINE=InnoDB;

-- Tabla Carreras
CREATE TABLE carreras (
    id INT PRIMARY KEY,
    nombre VARCHAR(100)
) ENGINE=InnoDB;

-- Tabla de Relación (Carrera-Módulo)
CREATE TABLE carrera_edificio (
    carrera_id INT NOT NULL,
    edificio_id INT NOT NULL,
    PRIMARY KEY (carrera_id, edificio_id),
    FOREIGN KEY (carrera_id) REFERENCES carreras(id),
    FOREIGN KEY (edificio_id) REFERENCES edificio(id)
);

-- Tabla Cursos
CREATE TABLE cursos (
    id_curso INT ,
    nombre_curso VARCHAR(100),
    duracion_periodo INT NOT NULL,
    numero_semestre INT NOT NULL,
    PRIMARY KEY (id_curso)
) ENGINE=InnoDB;
-- Tabla que relaciona las carreras con los cursos
CREATE TABLE carrera_cursos (
    carrera_id INT NOT NULL,
    curso_id INT NOT NULL,
    PRIMARY KEY (carrera_id, curso_id)
) ENGINE=InnoDB;

-- Tabla Docentes_Cursos (relación muchos a muchos)
-- DOCENTES APTOS PARA IMPARTIR UN CURSO
CREATE TABLE docentes_cursos (
    docente_id INT,
    curso_id INT,
    titular boolean default 0,
    PRIMARY KEY (docente_id, curso_id),
    FOREIGN KEY (docente_id) REFERENCES docentes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
) ENGINE=InnoDB;

-- Tabla de salones exclusivos para cursos
CREATE TABLE cursos_salones (
    salon_id INT,
    curso_id INT,

    PRIMARY KEY (salon_id, curso_id),
    FOREIGN KEY (salon_id) REFERENCES salones(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
) ENGINE=InnoDB;

-- ASIGNACIONES
-- Tabla Periodos de cursos
CREATE TABLE periodos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    edificio_id INT NOT NULL,
    FOREIGN KEY (edificio_id) REFERENCES edificio(id)

) ENGINE=InnoDB;
-- Diferentes horarios
CREATE TABLE horarios (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;


-- Tabla HorarioCursos
CREATE TABLE horario_cursos (
    id INT PRIMARY KEY AUTO_INCREMENT  NOT NULL,
    horario_id INT NOT NULL,
    curso_id INT NOT NULL,
    docente_id INT ,
    salon_id INT NOT NULL,
    seccion VARCHAR(5) NOT NULL,
    dias_semana VARCHAR(50),
    periodo_inicio INT NOT NULL,
    periodo_fin INT NOT NULL,
    FOREIGN KEY (horario_id) REFERENCES horarios(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id_curso),
    FOREIGN KEY (docente_id) REFERENCES docentes(id),
    FOREIGN KEY (salon_id) REFERENCES salones(id),
    FOREIGN KEY (periodo_inicio) REFERENCES periodos(id),
    FOREIGN KEY (periodo_fin) REFERENCES periodos(id)
) ENGINE=InnoDB;


-- (PRE-ASIGNACIONES)
-- Tabla Alumnos_Cursos (relación muchos a muchos con atributos extras)
CREATE TABLE alumnos_cursos (
    alumno_carnet INT NOT NULL,
    curso_id INT NOT NULL,
    semestre INT NOT NULL,
    ciclo INT NOT NULL,
    PRIMARY KEY (alumno_carnet, curso_id, semestre, ciclo),
    FOREIGN KEY (alumno_carnet) REFERENCES alumnos(carnet),
    FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
) ENGINE=InnoDB;
