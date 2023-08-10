USE cunoc;
INSERT INTO docentes (id, nombre, apellido, horario_entrada, horario_salida)
VALUES
    (35000, 'Moises', 'Granados', '14:00', '20:00'),
    (35003, 'Pedro', 'Dominguez', '14:00', '21:00'),
    (35006, 'Francisco', 'Rojas', '14:00', '21:00'),
    (35009, 'Mauricio', 'Lopez', '14:00', '19:00'),
    (35012, 'Cristian', 'Lopez', '14:00', '19:00'),
    (35015, 'Max', 'Cerna', '16:00', '19:00'),
    (35018, 'Claudia', 'Moran', '14:00', '20:00'),
    (35021, 'Rene', 'Orneliz', '14:00', '20:00'),
    (35024, 'Oliver', 'Sierra', '16:00', '17:00'),
    (35027, 'Deiffy', 'Morales', '14:00', '19:00'),
    (35030, 'Carlos', 'Lam', '14:00', '17:00'),
    (35033, 'Cesar', 'Grijalva', '14:00', '20:00'),
    (35036, 'Daniel', 'Quintana', '16:00', '17:00'),
    (35039, 'Karin', 'Rivas', '14:00', '17:00'),
    (35042, 'Coralia', 'Coralia', '14:00', '17:00'),
    (35045, 'Eddie', 'Flores', '14:00', '20:00'),
    (35048, 'Jorge', 'Rivera', '14:00', '17:00'),
    (35051, 'Humberto', 'Hernandez', '14:00', '20:00'),
    (35054, 'Alicia', 'Armas', '14:00', '17:00'),
    (35057, 'Santiago', 'Pineda', '14:00', '17:00'),
    (35060, 'Diego', 'Orozco', '14:00', '20:00'),
    (35063, 'Nery', 'Perez', '14:00', '20:00'),
    (35066, 'Alvaro', 'Flores', '16:00', '19:00'),
    (35069, 'Ernesto', 'Aguilar', '14:00', '19:00'),
    (35072, 'Ariel', 'Perez', '14:00', '20:00'),
    (35075, 'Alvaro', 'Ordonez', '14:00', '20:00'),
    (35078, 'Bruno', 'Coyoy', '14:00', '20:00'),
    (35081, 'Juan Jose', 'Maldonado', '14:00', '19:00'),
    (35084, 'Hector', 'Xicara', '14:00', '19:00'),
    (35087, 'Maria Rene', 'Martinez', '14:00', '20:00'),
    (35090, 'Daniel', 'Velasquez', '14:00', '20:00'),
    (35093, 'Otto', 'Soto', '14:00', '20:00'),
    (35096, 'Jorge', 'Aparicio', '16:00', '20:00'),
    (35099, 'Olimpia', 'Martinez', '14:00', '18:00'),
    (35102, 'Fernando', 'Caja', '15:00', '19:00'),
    (35105, 'Luis', 'Aballi', '15:00', '19:00');

INSERT INTO mobiliario (id, nombre)
VALUES
(1, 'Escritorios'),
(2, 'Mesas de dibujo'),
(3, 'Mesas de trabajo'),
(4, 'Butacas'),
(5, 'Sillas');

INSERT INTO edificio (id, nombre)
VALUES
(1, 'Modulo G'),
(2, 'Modulo 90'),
(3, 'Modulo E');

INSERT INTO salones (id, nombre, capacidad, tipo_mobiliario, edificio_id, disponible)
VALUES
(1, 'Salon 1',90, 5,1, 1),
(2, 'Salon 2',90, 1,1, 1),
(3, 'Salon 3',90, 1,1, 1),
(4, 'Salon 4',90, 1,1, 1),
(5, 'Salon 5',90, 1,1, 1),
(6, 'Salon 6',90, 1,1, 1),
(7, 'Salon 7',90, 1,1, 1),
(8, 'Salon 8',90, 1,1, 1),
(9, 'Salon 9',90, 1,1, 1),
(10, 'Salon 10',90, 1,1, 1),
(11, 'Salon 11',90, 1,1, 1),
(12, 'Salon 12',90, 1,1, 1),
(13, 'Hugo Pineda',30, 4,1, 1),
(14, 'Lab Fisica',60, 1,1, 1),
(15, 'Lab Aguas',60, 1,1, 1),
(16, 'Lab Industrial',60, 3 ,1, 1),
(17, 'Lab Quimica',60, 5,1, 1),
(18, 'Salon Mayor',60, 4,1, 1),
(19, 'Salon de Dibujo',90, 2,1, 1),
(20, 'Lab Electrica',60, 3 ,1, 1);

INSERT INTO carreras (id, nombre)
VALUES
(1, 'Ingenieria Civil'),
(2, 'Ingenieria Mecanica'),
(3, 'Ingenieria Industrial'),
(4, 'Ingenieria Mecanica Industrial'),
(5, 'Ingenieria en Ciencias y Sistemas');

INSERT INTO cursos (id_curso, id_carrera, nombre_curso, duracion_periodo, numero_semestre)
VALUES
(2796, 5, 'Introduccion a la programacion 1', 1, 3),
(2797, 5, 'Logica de Sistemas', 1, 3),
(2804, 5, 'Organizacion Computacional', 1, 5),
(2805, 5, 'Estructura De Datos', 1, 5),
(2907, 5, 'Practica Inicial TI', 1, 5),
(2816, 5, 'Redes de Computadoras 1', 1, 1),
(795, 5, 'Investigacion de Operaciones 2', 1, 7),
(2814, 5, 'Sistemas Operativos 1', 1, 7),
(2802, 5, 'Analisis Probabilistico', 1, 5),
(2815, 5, 'Arquiotectura de Computadoras 2', 1, 7),
(2827, 5, 'Analisis y Diseno de sistemas 2', 1, 9),
(2803, 5, 'Organizacion de lenguajes y Compiladores 1', 1, 5),
(2818, 5, 'Practica Intermedia TI', 1, 7),
(2824, 5, 'Modelacion y Simulacion 1', 1, 9),
(2813, 5, 'Teoria de Sistemas 2', 1, 7),
(2817, 5, 'Sistemas de Bases de Datos 1', 1, 7),
(2826, 5, 'Inteligencia Artificial', 1, 9),
(2828, 5, 'Seminario de Sistemas 2', 1, 9),
(950, 5, 'Estadistica 2', 1, 5);

INSERT INTO periodos (id, nombre, hora_inicio, hora_fin)
VALUES
(1, '1','13:40','14:30'),
(2, '2','14:30','15:20'),
(3, '3','15:20','16:10'),
(4, '4','16:10','17:00'),
(5, '5','17:00','17:50'),
(6, '6','17:50','18:40'),
(7, '7','18:40','19:30'),
(8, '8','19:30','20:20'),
(9, '9','20:20','21:10');