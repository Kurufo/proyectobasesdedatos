from dataclasses import dataclass, astuple, asdict, fields
import random

import csv
from typing import Optional

REGIONES = {
    '1': 'Arica-Parinacota',
    '2': 'Tarapacá',
    '3': 'Antofagasta',
    '4': 'Atacama',
    '5': 'Coquimbo',
    '6': 'Valparaíso',
    '7': 'Metropolitana',
    '8': 'O\'Higgins',
    '9': 'Maule',
    '10': 'Ñuble',
    '11': 'Bío Bío',
    '12': 'Araucanía',
    '13': 'Los Ríos',
    '14': 'Los Lagos',
    '15': 'Aysén',
    '16': 'Magallanes',
}

COLORES = {
    'blanco': 1,
    'pardo': 2,
    'tornasol': 3,
    'anaranjado': 4,
    'gris': 5,
    'cafe': 6,
    'ocre': 7,
    'rojo': 8,
    'castaño': 9,
    'verde': 10,
    'azul': 11,
    'amarillo': 12,
    'negro': 13,
}

@dataclass(frozen=True)
class FotoAve:
    dir_foto: str

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int:
                out.append(str(value))

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.foto_ave({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class SeEncuentraEn:
    especie: str
    nombre: str

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.se_encuentra_en({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class Ubicacion:
    nombre: str
    tipo_localidad: str
    region: str

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.ubicacion({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class Sujeto:
    especie: str
    dir_foto: str

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.sujeto({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class QueHace:
    especie: str
    id_comportamiento_nrml: int

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.que_hace({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class ComoLuce:
    especie: str
    id_apariencia_nrml: int

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.como_luce({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class AparienciaNormal:
    id_apariencia_nrml: Optional[int]
    tamano: str
    alas: str
    pico: str
    patas: str

    def __eq__(self, other):
        return astuple(self)[1:] == astuple(other)[1:]

    def __hash__(self):
        return hash(astuple(self)[1:])

    def set_id(self, id: int):
        fields = asdict(self)

        del fields['id_apariencia_nrml']

        return AparienciaNormal(id_apariencia_nrml=id, **fields)

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.apariencia_normal({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class AparienciaNormalColor:
    id_apariencia_nrml: Optional[int]
    id_color: Optional[int]

    def __eq__(self, other):
        return astuple(self)[1:] == astuple(other)[1:]

    def __hash__(self):
        return hash(astuple(self)[1:])

    def set_id(self, id: int):
        fields = asdict(self)

        del fields['id_apariencia_nrml']

        return AparienciaNormal(id_apariencia_nrml=id, **fields)

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.apariencia_observada__color({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class ComportamientoNormal:
    id_comportamiento_nrml: Optional[int]

    alimentacion: str
    nidificacion: str
    migracion: bool
    cronotipo: str

    def __eq__(self, other):
        return astuple(self)[1:] == astuple(other)[1:]

    def __hash__(self):
        return hash(astuple(self)[1:])

    def set_id(self, id: int):
        fields = asdict(self)
        del fields['id_comportamiento_nrml']
        return ComportamientoNormal(id_comportamiento_nrml=id, **fields)
    
    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == Optional[int] or field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.comportamiento_normal({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True, eq=True)
class Ave:
    especie: str
    nombre: str
    orden: str
    familia: str
    habitat: str

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int:
                out.append(str(value))

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.ave({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


def get_bird_data(data_dir: str):
    data = {
        'aves': set(),
        'comportamientos_normales': set(),
        'apariencias_normales': set(),
        'fotos': set(),
        'como_luce': set(),
        'que_hace': set(),
        'sujeto': set(),
        'foto_ave': set(),
        'color': set()
    }

    with open(data_dir, 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';', dialect='excel')

        for row in reader:
            comportamiento_normal = ComportamientoNormal(
                id_comportamiento_nrml=None,
                alimentacion=row['Alimentación'].strip(),
                nidificacion=row['Nidificación'].strip(),
                migracion=True if row['Migración'] != 'Sí' else False,
                cronotipo=row['Cronotipo'].strip(),
            )

            comportamientos_normales = data['comportamientos_normales']

            if comportamiento_normal not in data['comportamientos_normales']:
                comportamiento_normal = comportamiento_normal.set_id(len(comportamientos_normales) + 1)
                comportamientos_normales.add(comportamiento_normal)
            else:
                comportamiento_normal = comportamientos_normales.union({comportamiento_normal}).pop()


            apariencia_normal = AparienciaNormal(
                id_apariencia_nrml=None,
                tamano=row['Tamaño'].strip(),
                patas=row['Patas'].strip(),
                alas=row['Alas'].strip(),
                pico=row['Picos'].strip(),
            )

            apariencias_normales = data['apariencias_normales']

            if apariencia_normal not in data['apariencias_normales']:
                apariencia_normal = apariencia_normal.set_id(len(apariencias_normales) + 1)
                apariencias_normales.add(apariencia_normal)
            else:
                apariencia_normal = apariencias_normales.union({apariencia_normal}).pop()

            for color in row['Color'].strip().split(';'):
                data['color'].add(AparienciaNormalColor(id_apariencia_nrml=apariencia_normal.id_apariencia_nrml, id_color=COLORES[color]))


            data['aves'].add(Ave(
                nombre=row['Ave'].strip(),
                especie=row['Especie'].strip(),
                orden=row['Orden'].strip(),
                familia=row['Familia'].strip(),
                habitat=row['Hábitat'].strip(),
                # estado_conservacion=random.choice(['contaminación', 'sequía', 'bien conservado'])
            ))

            data['como_luce'].add(ComoLuce(
                especie=row['Especie'].strip(),
                id_apariencia_nrml=apariencia_normal.id_apariencia_nrml
            ))

            data['que_hace'].add(QueHace(
                especie=row['Especie'].strip(),
                id_comportamiento_nrml=comportamiento_normal.id_comportamiento_nrml
            ))

            data['sujeto'].add(Sujeto(
                especie=row['Especie'].strip(),
                dir_foto=row['Foto'].strip(),
            ))

            data['foto_ave'].add(FotoAve(row['Foto'].strip()))

    return data


def fetch_location_data(data_dir: str, random_estado_conservacion=False):
    with open(data_dir, 'r', encoding='cp1252') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';', dialect='excel')

        for row in reader:
            yield Ubicacion(
                nombre=row.get('Ciudad').strip(),
                tipo_localidad=row.get('Localidad').strip(),
                region=REGIONES.get(row.get('Region')).strip(),
            )


def fetch_location_from_id(data_dir: str, id_ciudad: str):
    with open(data_dir, 'r', encoding='cp1252') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';', dialect='excel')

        for row in reader:
            if row.get('id_ciudad') is None:
                continue
            if id_ciudad == row.get('id_ciudad').strip():
                return row.get('Ciudad').strip()


def fetch_photo_from_bird(especie: str):
    with open('aves.csv', 'r', encoding='cp1252') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';', dialect='excel')

        for row in reader:
            if especie == row.get('Especie').strip():
                return row.get('Foto').strip()


def fetch_bird_location(data_dir: str):
    with open(data_dir, 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';', dialect='excel')

        ciudades = set()

        for row in reader:
            parse_regiones = [region for region in row.get('Regiones').split(sep=',') if region != '']

            regiones = set()

            for parse_region in parse_regiones:
                rango_regiones = parse_region.split(sep=':')

                if len(rango_regiones) == 2:
                    for numero_region in range(int(rango_regiones[0]), int(rango_regiones[1]) + 1):
                        regiones.add(REGIONES[str(numero_region)])
                if len(rango_regiones) == 1:
                    regiones.add(REGIONES[str(int(rango_regiones[0]))])

            if regiones:
                for ubicacion in fetch_location_data('localidades.csv'):
                    if ubicacion.region.strip() in regiones:
                        ciudades.add(SeEncuentraEn(especie=row['Especie'].strip(), nombre=ubicacion.nombre))
                continue

            for id_ciudad in row.get('Ciudades').split(sep=','):
                id_ciudad = id_ciudad.strip()

                se_encuentra_en = SeEncuentraEn(especie=row['Especie'].strip(), nombre=fetch_location_from_id('localidades.csv', id_ciudad))
                ciudades.add(se_encuentra_en)

        return ciudades


if __name__ == '__main__':
    sql_fotos = []

    for foto in get_bird_data('datos_aves_final.csv').get('foto_ave'):
        sql_fotos.append(foto)

    sql_datos_aves = []
    for k, v in get_bird_data('datos_aves_final.csv').items():
        if k == 'foto_ave':
            continue

        for value in v:
            sql_datos_aves.append(value)

    from itertools import chain

    todo = chain(sql_fotos, sql_datos_aves, list(fetch_location_data('localidades.csv')), list(fetch_bird_location('aves_localidades2.csv')))

    with open('datos_aves.sql', 'w') as f:
        for valor in todo:
            f.write(valor.as_sql_insert() + '\n')
