from dataclasses import dataclass, fields, astuple
import random
from typing import List, Optional
from time import sleep
from datetime import datetime, timedelta

import requests
import json


@dataclass(frozen=True)
class FechaYHora:
    fecha_hora: datetime

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int:
                out.append(str(value))
            elif field.type == datetime:
                value: datetime
                out.append("'" + value.isoformat(sep=' ') + "Z'")

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.fecha_y_hora({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'



@dataclass(frozen=True)
class ComoLucia:
    id_avistamiento: int
    id_apariencia_obs: int

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
        return f'INSERT INTO aves.como_lucia({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class QueHacia:
    id_avistamiento: int
    id_comportamiento_obs: int

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
        return f'INSERT INTO aves.que_hacia({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'



@dataclass(frozen=True)
class AparienciaObservada:
    id_apariencia_obs: int

    tamano: str
    alas: str
    pico: str
    obs_adicional: str

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
        return f'INSERT INTO aves.apariencia_observada({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class ComportamientoObservado:
    id_comportamiento_obs: int

    alimentacion: str
    nidificacion: str
    migracion: bool
    cronotipo: str
    obs_adicional: str

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int:
                out.append(str(value))
            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.comportamiento_observado({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class Cuando:
    fecha_hora: datetime
    id_avistamiento: int

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int:
                out.append(str(value))
            elif field.type == datetime:
                value: datetime
                out.append("'" + value.isoformat(sep=' ') + "Z'")

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.cuando({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class AvistadoEn:
    dir_foto: str
    id_avistamiento: int

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
        return f'INSERT INTO aves.avistado_en({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class Avistado:
    especie: str
    id_avistamiento: int

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
        return f'INSERT INTO aves.avistado({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class VistoEn:
    nombre: str
    id_avistamiento: int

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
        return f'INSERT INTO aves.visto_en({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class HechoPor:
    username: str
    id_avistamiento: int

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
        return f'INSERT INTO aves.hecho_por({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class Avistamiento:
    id_avistamiento: int
    estado: str
    nido: bool
    sexo: str
    estado_conservacion: str
    reportado: bool

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int:
                out.append(str(value))

            elif field.type == bool:
                out.append(str(value).upper())

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.avistamiento({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class Avistador:
    username: str
    intencion: Optional[str]

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if value is None:
                out.append('NULL')
                continue

            if field.type == Optional[str] or field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int:
                out.append(str(value))

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.avistador({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'

@dataclass(frozen=True)
class Investigador:
    username: str
    institucion: str
    identificacion_nacional: str

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
        return f'INSERT INTO aves.investigador({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class Usuario:
    username: str
    contrasena: str

    nombre_usuar: str
    apellido: str

    fecha_nacimiento: str

    email: str

    dir_foto_usr: str

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
        return f'INSERT INTO aves.usuario({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


@dataclass(frozen=True)
class CondicionesClimaticas:
    nombre: str
    fecha_hora: datetime
    precipitacion: float
    temperatura: float
    humedad: float
    veloc_viento: int
    presion_atm: float
    cota_nieve: int

    def comma_separated_fields(self) -> str:
        return ','.join((field.name for field in fields(self.__class__)))

    def comma_separated_values(self) -> str:
        out = []

        for value, field in zip(astuple(self), fields(self)):
            if field.type == str:
                out.append("'" + str(value) + "'")
            elif field.type == int or field.type == float:
                out.append(str(value))
            elif field.type == datetime:
                value: datetime
                out.append("'" + value.isoformat(sep=' ') + "Z'")

        return ','.join(out)

    def as_sql_insert(self):
        return f'INSERT INTO aves.condiciones_climaticas({self.comma_separated_fields()}) VALUES ({self.comma_separated_values()});'


def fetch_random_user(users_to_fetch: int = 50, debug=False):
    params = {
       'results': users_to_fetch,
       'inc': 'gender,location,nat,picture,email,data,login,name,dob',
    }

    response = requests.get('https://randomuser.me/api/', params=params)

    response_json = json.loads(response.content)

    if debug:
        print(response_json)

    for user_json in response_json.get('results'):
        login_data = user_json.get('login')
        name_data = user_json.get('name')

        yield Usuario(
            username=login_data.get('username'),
            contrasena=login_data.get('password'),
            email=user_json.get('email'),
            fecha_nacimiento=' '.join(user_json.get('dob').get("date").split(sep='T')),

            nombre_usuar=name_data.get('first'),
            apellido=name_data.get('last'),
            dir_foto_usr=user_json.get('picture').get('large'),
        )


def fetch_random_location_chile_fromapi():
    response = requests.get('https://api.3geonames.org/?randomland=CL&json=1')
    response_json = json.loads(response.content)

    ubicacion_mas_proxima = response_json.get('nearest')
    region = ubicacion_mas_proxima.get('prov')
    nombre = ubicacion_mas_proxima.get('city')

    if not (bool(nombre) and bool(region)):
        raise ValueError('Ubicación inválida.')

    region = region.lower()

    if 'arica' in region:
        region = 'Arica-Parinacota'
    elif 'antofagasta' in region:
        region = 'Antofagasta'
    elif 'tarapaca' in region or 'tarapacá' in region:
        region = 'Antofagasta'
    elif 'coquimbo' in region:
        region = 'Coquimbo'
    elif 'valparaíso' in region or 'valparaiso' in region:
        region = 'Valparaíso'
    elif 'metropolitana' in region or 'santiago' in region or 'metropolitan' in region:
        region = 'Metropolitana'
    elif 'higgins' in region:
        region = 'O\'Higgins'
    elif 'maule' in region:
        region = 'Maule'
    elif 'nuble' in region or 'ñuble' in region:
        region = 'Ñuble'
    elif 'bio-bio' in region or 'bíobío' in region or 'biobio' in region or 'biobío' in region:
        region = 'Bío Bío'
    elif 'araucanía' in region or 'araucania' in region:
        region = 'Araucanía'
    elif 'los ríos' in region or 'los rios' in region or 'rios' in region or 'ríos' in region:
        region = 'Los Ríos'
    elif 'los lagos' in region or 'lagos' in region:
        region = 'Los Lagos'
    elif 'aysén' in region or 'aysen' in region:
        region = 'Aysén'
    elif 'magallanes' in region:
        region = 'Magallanes'
    else:
        raise ValueError('Error al normalizar la región.')

    return nombre, region


def fetch_random_locations_from_api():
    with open('valid_loc_cl.txt', 'w+') as f:
        valid_locations = 0

        while(valid_locations < 1000):
            try:
                nombre, region = fetch_random_location_chile_fromapi()
            except:
                continue

            f.write(f'{nombre},{region}\n')
            valid_locations += 1

            sleep(0.1)


def forward_geocoding(nombre: str, region: str):
    response = requests.get(f'https://geocode.xyz/{nombre}+{region}+chile?json=1&auth=173296625396405313589x7158')
    response_json = json.loads(response.content)

    latitud = response_json.get('latt')
    longitud = response_json.get('longt')

    return {
        'lat': str(latitud),
        'long': str(longitud),
    }


def fetch_weather_conditions_for_city(nombre: str, region: str, fecha_hora: datetime):
    data = forward_geocoding(nombre, region)

    date = str(fecha_hora).split(sep=' ')[0]

    latitud = data.get('lat')
    longitud = data.get('long')

    params = {
        'start_date': date,
        'end_date': date,
        'latitude': latitud,
        'longitude': longitud,
        'daily': ('temperature_2m_max', 'temperature_2m_min', 'precipitation_sum', 'rain_sum', 'snowfall_sum', 'windspeed_10m_max', 'winddirection_10m_dominant', 'shortwave_radiation_sum'),
        'hourly': ('relativehumidity_2m', 'windspeed_10m', 'pressure_msl'),
        'timezone': 'GMT+0',
    }

    response = requests.get('https://archive-api.open-meteo.com/v1/era5', params=params)
    response_json = json.loads(response.content)

    weather_daily = response_json.get('daily')
    weather_hourly = response_json.get('hourly')
    avg_temp = (weather_daily.get('temperature_2m_max')[0] - weather_daily.get('temperature_2m_min')[0]) / 2

    humedad = random.choice(weather_hourly.get('relativehumidity_2m'))
    veloc_viento = random.choice(weather_hourly.get('windspeed_10m'))
    pressure_msl = random.choice(weather_hourly.get('pressure_msl'))

    return CondicionesClimaticas(
        nombre=nombre,
        fecha_hora=fecha_hora,
        precipitacion=weather_daily.get('rain_sum')[0],
        temperatura=avg_temp,
        humedad=humedad,
        veloc_viento=veloc_viento,
        presion_atm=pressure_msl,
        cota_nieve=weather_daily.get('snowfall_sum')[0]
    )

@dataclass(frozen=True)
class AparienciaObservadaColor:
    id_apariencia_obs: int
    id_color: int

def indentificacion_nacional_aleatoria():
    return ''.join([str(random.randint(0, 9)) for _ in range(7)]) + '-' + str(random.randint(0, 9))


if __name__ == '__main__':
    usuarios = []
    investigadores = []
    avistadores = []

    for usuario in fetch_random_user():
        variable_aleatoria = random.randint(0, 9)

        instituciones = ['Universidad de la Vida',
                         'Universidad de Miskatonic',
                         'Universidad de Colo Colo',
                         'Instituto Aplaplac']

        if variable_aleatoria < 2:
            investigador = Investigador(username=usuario.username,
                                        institucion=random.choice(instituciones),
                                        identificacion_nacional=indentificacion_nacional_aleatoria())

            investigadores.append(investigador)

        else:
            intenciones = ['Ver aves', 'Aprender sobre aves', None]

            avistador = Avistador(username=usuario.username, intencion=random.choice(intenciones))

            avistadores.append(avistador)

        usuarios.append(usuario)

    avistamientos = []
    hechos_por = []
    vistos_en = []
    avistado = []
    se_encuentran_en = []
    avistados_en = []
    comportamientos_observados = []
    apariencias_observadas = []
    cuandos = []
    condiciones_climaticas = []
    que_hacian = []
    como_lucian = []
    fechas_y_horas = []
    apariencias_observadas_colores = []

    for id_avistamiento in range(1, 250):
        avistamientos.append(
            Avistamiento(
                id_avistamiento=id_avistamiento,
                estado='muerto' if random.randint(0, 9) < 1 else 'vivo',
                nido=bool(random.randint(0, 1)),
                sexo='macho' if random.randint(0, 1) else 'hembra',
                reportado=random.randint(0, 999) < 1,
                estado_conservacion=random.choice(['contaminación', 'sequía', 'bien conservado'])
            )
        )

        hechos_por.append(
            HechoPor(
                username=random.choice(usuarios).username,
                id_avistamiento=id_avistamiento,
            )
        )

        from queries import fetch_location_data, fetch_bird_location, get_bird_data, fetch_photo_from_bird

        ubicaciones = fetch_location_data('localidades.csv', True)

        especie_ave_aleatoria = random.choice(list(get_bird_data('datos_aves_final.csv').get('aves'))).especie

        avistado.append(
            Avistado(
                especie=especie_ave_aleatoria,
                id_avistamiento=id_avistamiento,
            )
        )

        lugar_aleatorio_tipico  = random.choice([se_encuentra_en for se_encuentra_en in fetch_bird_location('aves_localidades2.csv') if se_encuentra_en.especie == especie_ave_aleatoria])

        vistos_en.append(
            VistoEn(
                nombre=lugar_aleatorio_tipico.nombre,
                id_avistamiento=id_avistamiento,
            )
        )
        foto_de_especie_aleatoria = fetch_photo_from_bird(especie_ave_aleatoria)

        avistados_en.append(AvistadoEn(
            dir_foto=foto_de_especie_aleatoria,
            id_avistamiento=id_avistamiento,
        ))

        fecha_hora = datetime.now() - timedelta(weeks=2, days=id_avistamiento)
        fechas_y_horas.append(FechaYHora(fecha_hora=fecha_hora))
        condiciones_climaticas.append(fetch_weather_conditions_for_city('Concepción', 'Bío Bío', fecha_hora))

        cuandos.append(Cuando(
            fecha_hora=fecha_hora,
            id_avistamiento=id_avistamiento
        ))

        nuevo_id_comportamiento_obs = len(comportamientos_observados) + 1

        comportamientos_observados.append(ComportamientoObservado(
            id_comportamiento_obs=nuevo_id_comportamiento_obs,
            alimentacion=random.choice(('herbívoro', 'carnívoro', 'nectarívoro', 'insectívoro')),
            nidificacion=random.choice(('escarbado', 'montículo', 'madriguera', 'cuenco')),
            migracion=bool(random.randint(0, 1)),
            cronotipo=random.choice(('nocturno', 'diurno', 'crepuscular', 'diurno - nocturno')),
            obs_adicional='aasdasdasdasdasd'
        ))

        colores = ('negro',
                   'gris',
                   'pardo',
                   'blanco',
                   'blanco - negro',
                   'blanco - negro - castaño rojizo',
                   'blanco - negro - ocre',
                   'blanco - negro - pardo',
                   'blanco - negro - gris',
                   'blanco - negro - anaranjado',
                   'blanco - negro - amarillo',
                   'blanco - gris',
                   'blanco - gris - pardo',
                   'blanco - pardo - ocre',
                   'blanco - pardo',
                   'castaño - gris',
                   'pardo - castaño - gris',
                   'pardo - gris - negro',
                   'pardo/pardo - negro - rojo',
                   'pardo - rojo - negro',
                   'blanco/pardo',
                   'gris - castaño rojizo',
                   'gris - pardo',
                   'gris - pardo - ocre',
                   'gris - pardo - rojo',
                   'gris - café',
                   'gris - pardo rojizo',
                   'tornasol',
                   'tornasol - blanco',
                   'gris - anaranjado',
                   'anaranjado',
                   'rosado',
                   'rojo',
                   'verde',
                   'amarillo')

        nuevo_id_apariencia_obs = len(apariencias_observadas) + 1

        from queries import COLORES
        import csv

        with open('datos_aves_final.csv', 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';', dialect='excel')

            for row in reader:
                if row['Especie'].strip() != especie_ave_aleatoria:
                    continue

                for color in row['Color'].strip().split(';'):
                    apariencias_observadas_colores.append(AparienciaObservadaColor(id_color=(COLORES[color]), id_apariencia_obs=COLORES))

        apariencias_observadas.append(AparienciaObservada(
            id_apariencia_obs=nuevo_id_apariencia_obs,
            tamano=random.choice(('grande', 'muy grande' , 'pequeño', 'mediano - grande', 'mediano - pequeño')),
            alas=random.choice(('de planeo', 'elevadoras', 'elípticas')),
            pico=random.choice(('granívoro', 'insectívoro', 'nectarívoro', 'carpintero', 'pico - bolsa', 'filtrador')),
            obs_adicional='asdasdasdasdda'
        ))


        que_hacian.append(QueHacia(
            id_avistamiento=id_avistamiento,
            id_comportamiento_obs=nuevo_id_comportamiento_obs
        ))

        como_lucian.append(ComoLucia(
            id_avistamiento=id_avistamiento,
            id_apariencia_obs=nuevo_id_apariencia_obs
        ))

    from itertools import chain

    todo = chain(usuarios,
                 investigadores,
                 avistadores,
                 avistamientos,
                 fechas_y_horas,
                 hechos_por,
                 vistos_en,
                 avistado,
                 se_encuentran_en,
                 avistados_en,
                 comportamientos_observados,
                 apariencias_observadas,
                 cuandos,
                 condiciones_climaticas,
                 que_hacian,
                 como_lucian)

    ocupaciones = ['Abogado',
                   'Arquitecto',
                   'Ingeniero',
                   'Fotografo',
                   'Actor',
                   'Peluquero',
                   'Economista',
                   'Vendedor',
                   'Administrador',
                   "Diseñador",
                   'Profesor',
                   'Auxiliar',
                   'Médico',
                   'Constructor',
                   'Biólogo',
                   'Físico de Partículas',
                   'Doctor de Perritos']

    with open('datos_inventados.sql', 'w', encoding='utf-8') as f:
        for obj in todo:
            f.write(obj.as_sql_insert() + '\n')
