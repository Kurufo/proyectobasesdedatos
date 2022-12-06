DROP SCHEMA aves CASCADE;

CREATE SCHEMA aves;

CREATE TABLE aves.avistamiento
(
    id_avistamiento     INT PRIMARY KEY,
    estado              VARCHAR(6) CHECK (estado IN ('vivo', 'muerto')),
    nido                BOOLEAN,
    sexo                VARCHAR(6) CHECK (sexo IN ('macho', 'hembra')),
    reportado           BOOLEAN,
    estado_conservacion VARCHAR(17) CHECK (estado_conservacion IN ('contaminación', 'sequia', 'bien conservado'))
);


CREATE TABLE aves.ubicacion
(
    nombre         VARCHAR(100) PRIMARY KEY,
    tipo_localidad VARCHAR(6) CHECK (tipo_localidad IN ('ciudad',
                                                        'villa',
                                                        'pueblo',
                                                        'rural',
                                                        'costa',
                                                        'oasis')),
    region         VARCHAR(20) CHECK (region IN ('Arica-Parinacota',
                                                 'Tarapacá',
                                                 'Antofagasta',
                                                 'Atacama',
                                                 'Coquimbo',
                                                 'Valparaíso',
                                                 'Metropolitana',
                                                 'O''Higgins',
                                                 'Maule',
                                                 'Ñuble',
                                                 'Bío Bío',
                                                 'Araucanía',
                                                 'Los Ríos',
                                                 'Los Lagos',
                                                 'Aysén',
                                                 'Magallanes'))
);

CREATE TABLE aves.visto_en
(
    nombre          VARCHAR(100) REFERENCES aves.ubicacion,
    id_avistamiento INT REFERENCES aves.avistamiento,
    PRIMARY KEY (nombre, id_avistamiento)
);

CREATE TABLE aves.fecha_y_hora
(
    fecha_hora TIMESTAMP WITH TIME ZONE PRIMARY KEY
);

CREATE TABLE aves.condiciones_climaticas
(
    nombre        VARCHAR(100) REFERENCES aves.ubicacion,
    fecha_hora    TIMESTAMP WITH TIME ZONE REFERENCES aves.fecha_y_hora,
    precipitacion FLOAT,
    temperatura   FLOAT,
    humedad       FLOAT,
    veloc_viento  INT,
    presion_atm   FLOAT,
    cota_nieve    INT,
    PRIMARY KEY (nombre, fecha_hora)
);

CREATE TABLE aves.cuando
(
    fecha_hora      TIMESTAMP WITH TIME ZONE REFERENCES aves.fecha_y_hora,
    id_avistamiento INT REFERENCES aves.avistamiento,
    PRIMARY KEY (fecha_hora, id_avistamiento)
);

CREATE TABLE aves.foto_ave
(
    dir_foto VARCHAR(500) PRIMARY KEY
);

CREATE TABLE aves.avistado_en
(
    dir_foto        VARCHAR(500) REFERENCES aves.foto_ave,
    id_avistamiento INT REFERENCES aves.avistamiento,
    PRIMARY KEY (dir_foto, id_avistamiento)
);

CREATE TABLE aves.usuario
(
    username         VARCHAR(100) PRIMARY KEY,
    contrasena       VARCHAR(50)  NOT NULL,
    nombre_usuar     VARCHAR(50),
    apellido         VARCHAR(50),
    fecha_nacimiento DATE,
    ocupacion        VARCHAR(100),
    nacionalidad     VARCHAR(100),
    email            VARCHAR(100) NOT NULL,
    dir_foto_usr     VARCHAR(500)
);

CREATE TABLE aves.hecho_por
(
    username        VARCHAR(100) REFERENCES aves.usuario,
    id_avistamiento INT REFERENCES aves.avistamiento,
    PRIMARY KEY (id_avistamiento)
);

CREATE TABLE aves.avistador
(
    username  VARCHAR(100) REFERENCES aves.usuario ON DELETE CASCADE,
    intencion VARCHAR(100),
    PRIMARY KEY (username)
);


CREATE TABLE aves.investigador
(
    username                VARCHAR(100) REFERENCES aves.usuario ON DELETE CASCADE,
    institucion             VARCHAR(100) NOT NULL,
    linea_investigacion     VARCHAR(100),
    identificacion_nacional VARCHAR(12) NOT NULL,
    PRIMARY KEY (username)
);


CREATE TABLE aves.apariencia_normal
(
    id_apariencia_nrml INT PRIMARY KEY,
    tamano             VARCHAR(20) CHECK (tamano IN ('pequeno',
                                                     'mediano - pequeno',
                                                     'mediano - grande',
                                                     'muy pequeno',
                                                     'grande',
                                                     'muy grande',
                                                     'mediano')),
    alas               VARCHAR(40) CHECK (alas IN ('de planeo',
                                                   'elevadoras',
                                                   'elipticas',
                                                   'de alta velocidad',
                                                   'terrestre poco voladora',
                                                   'terrestre no voladora',
                                                   'acuatica no voladora')),
    pico               VARCHAR(20) CHECK (pico IN ('generalista',
                                                   'insectivoro',
                                                   'granivoro',
                                                   'nectarivoro',
                                                   'frugivoro',
                                                   'carpintero',
                                                   'pico - bolsa',
                                                   'limicola',
                                                   'filtrador',
                                                   'pescador',
                                                   'pescador grueso',
                                                   'pescador ganchudo',
                                                   'buceador',
                                                   'carroñero',
                                                   'ave de presa',
                                                   'plano',
                                                   'plano c/caruncula')),
    patas              VARCHAR(20) CHECK (patas IN ('rapaces',
                                                    'paserinas',
                                                    'palmeadas',
                                                    'cigodactilas',
                                                    'espoloneadas',
                                                    'pectinadas',
                                                    'lagopedo',
                                                    'semipalmeadas',
                                                    'pamprodactilas',
                                                    'anisodactilas',
                                                    'totipalmeadas',
                                                    'lobulada'))
);

CREATE TABLE aves.apariencia_observada
(
    id_apariencia_obs INT PRIMARY KEY,
    tamano            VARCHAR(20) CHECK (tamano IN ('pequeno',
                                                    'mediano - pequeno',
                                                    'mediano - grande',
                                                    'grande',
                                                    'muy grande',
                                                    'mediano')),
    alas              VARCHAR(40) CHECK (alas IN ('de planeo',
                                                  'elevadoras',
                                                  'elipticas',
                                                  'de alta velocidad',
                                                  'terrestre poco voladora',
                                                  'terrestre no voladora',
                                                  'acuatica no voladora')),

    pico              VARCHAR(20) CHECK (pico IN ('generalista',
                                                  'insectivoro',
                                                  'granivoro',
                                                  'nectarivoro',
                                                  'frugivoro',
                                                  'carpintero',
                                                  'pico - bolsa',
                                                  'limicola',
                                                  'filtrador',
                                                  'pescador',
                                                  'pescador grueso',
                                                  'pescador ganchudo',
                                                  'buceador',
                                                  'carronero',
                                                  'ave de presa',
                                                  'plano',
                                                  'plano c/caruncula')),
    patas             VARCHAR(20) CHECK (patas IN ('rapaces',
                                                   'paserinas',
                                                   'palmeadas',
                                                   'cigodáctil',
                                                   'espoloneadas',
                                                   'pectinadas',
                                                   'lagópedo',
                                                   'semipalmeadas',
                                                   'pamprodáctilas',
                                                   'anisodáctilas',
                                                   'totipalmeadas',
                                                   'lóbulada')),
    obs_adicional     VARCHAR(1000)
);

CREATE TABLE aves.color
(
    id_color SERIAL PRIMARY KEY,
    nombre_color    VARCHAR(20) CHECK (nombre_color IN ('blanco',
                                                 'pardo',
                                                 'tornasol',
                                                 'anaranjado',
                                                 'gris',
                                                 'cafe',
                                                 'ocre',
                                                 'rojo',
                                                 'castaño',
                                                 'verde',
                                                 'azul',
                                                 'amarillo',
                                                 'negro'))
);

CREATE table aves.apariencia_normal__color
(
    id_apariencia_nrml INT REFERENCES aves.apariencia_normal,
    id_color           SERIAL REFERENCES aves.color
);

CREATE table aves.apariencia_observada__color
(
    id_apariencia_obs INT REFERENCES aves.apariencia_observada,
    id_color          SERIAL REFERENCES aves.color
);


INSERT INTO aves.color(nombre_color) VALUES ('blanco');
INSERT INTO aves.color(nombre_color) VALUES ('pardo');
INSERT INTO aves.color(nombre_color) VALUES ('tornasol');
INSERT INTO aves.color(nombre_color) VALUES ('anaranjado');
INSERT INTO aves.color(nombre_color) VALUES ('gris');
INSERT INTO aves.color(nombre_color) VALUES ('cafe');
INSERT INTO aves.color(nombre_color) VALUES ('ocre');
INSERT INTO aves.color(nombre_color) VALUES ('rojo');
INSERT INTO aves.color(nombre_color) VALUES ('castaño');
INSERT INTO aves.color(nombre_color) VALUES ('verde');
INSERT INTO aves.color(nombre_color) VALUES ('azul');
INSERT INTO aves.color(nombre_color) VALUES ('amarillo');
INSERT INTO aves.color(nombre_color) VALUES ('negro');

CREATE TABLE aves.comportamiento_normal
(
    id_comportamiento_nrml INT PRIMARY KEY,
    alimentacion           VARCHAR(20) CHECK (alimentacion IN ('carnivoro',
                                                               'granivoro',
                                                               'herbivoro',
                                                               'omnivoro',
                                                               'insectivoro',
                                                               'nectarivoro')),
    nidificacion           VARCHAR(20) CHECK (nidificacion IN ('escarbado',
                                                               'monticulo',
                                                               'madriguera',
                                                               'cavidad',
                                                               'cuenco',
                                                               'plato',
                                                               'plataforma',
                                                               'colgante',
                                                               'esférico')),
    migracion              BOOLEAN,
    cronotipo              VARCHAR(30) CHECK (cronotipo IN ('nocturno',
                                                            'diurno',
                                                            'diurno - nocturno',
                                                            'crepuscular',
                                                            'diurno - crepuscular',
                                                            'crepuscular - nocturno'))
);

CREATE TABLE aves.comportamiento_observado
(
    id_comportamiento_obs INT PRIMARY KEY,
    alimentacion          VARCHAR(20) CHECK (alimentacion IN ('carnivoro',
                                                              'herbivoro',
                                                              'omnivoro',
                                                              'insectivoro',
                                                              'nectarivoro')),
    nidificacion          VARCHAR(20) CHECK (nidificacion IN ('escarbado',
                                                              'monticulo',
                                                              'madriguera',
                                                              'cavidad',
                                                              'cuenco',
                                                              'plato',
                                                              'plataforma',
                                                              'colgante',
                                                              'esferico')),
    migracion             BOOLEAN,
    cronotipo             VARCHAR(30) CHECK (cronotipo IN ('nocturno', 'diurno',
                                                           'diurno - nocturno',
                                                           'crepuscular',
                                                           'diurno - crepuscular',
                                                           'crepuscular - nocturno')),
    obs_adicional         VARCHAR(1000)
);

-- Agregado selva

CREATE TABLE aves.ave
(
    especie VARCHAR(50) PRIMARY KEY,
    nombre  VARCHAR(50),
    orden   VARCHAR(50),
    familia VARCHAR(50),
    habitat VARCHAR(50) CHECK (habitat IN ('cerro',
                                           'pradera',
                                           'campo',
                                           'quebrada',
                                           'desierto polar',
                                           'montaña',
                                           'bosque',
                                           'desierto',
                                           'matorral',
                                           'jardin',
                                           'altiplano',
                                           'humedales',
                                           'mar abierto',
                                           'costa',
                                           'cordillera',
                                           'rio',
                                           'lago',
                                           'huerto',
                                           'plaza',
                                           'parque',
                                           'pelagico',
                                           'selva',
                                           'formacion de agua dulce',
                                           'pampa'))
);

CREATE TABLE aves.se_encuentra_en
(
    especie VARCHAR(50) REFERENCES aves.ave,
    nombre  VARCHAR(100) REFERENCES aves.ubicacion,
    PRIMARY KEY (especie, nombre)
);

CREATE TABLE aves.sujeto
(
    especie  VARCHAR(50) REFERENCES aves.ave,
    dir_foto VARCHAR(500) REFERENCES aves.foto_ave,
    PRIMARY KEY (especie, dir_foto)
);

CREATE TABLE aves.avistado
(
    especie         VARCHAR(50) REFERENCES aves.ave,
    id_avistamiento INT REFERENCES aves.avistamiento,
    PRIMARY KEY (especie, id_avistamiento)
);

CREATE TABLE aves.como_luce
(
    especie            VARCHAR(50) REFERENCES aves.ave,
    id_apariencia_nrml INT REFERENCES aves.apariencia_normal,
    PRIMARY KEY (especie, id_apariencia_nrml)
);

-- modificado

CREATE TABLE aves.como_lucia
(
    id_avistamiento           INT REFERENCES aves.avistamiento,
    id_apariencia_obs INT REFERENCES aves.apariencia_observada,
    PRIMARY KEY (id_avistamiento, id_apariencia_obs)
);

CREATE TABLE aves.que_hace
(
    especie                VARCHAR(50) REFERENCES aves.ave,
    id_comportamiento_nrml INT REFERENCES aves.comportamiento_normal,
    PRIMARY KEY (especie, id_comportamiento_nrml)
);

-- modificado

CREATE TABLE aves.que_hacia
(
    id_avistamiento INT REFERENCES aves.avistamiento,
    id_comportamiento_obs INT REFERENCES aves.comportamiento_observado,
    PRIMARY KEY (id_avistamiento, id_comportamiento_obs)
);
