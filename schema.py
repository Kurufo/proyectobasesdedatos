import psycopg
from dataclasses import dataclass
from flask_login import UserMixin
CONN_STRING = 'host=plop.inf.udec.cl port=5432 dbname=bdi2022bl user=bdi2022bl password=bdi2022bl'


class NoEncontradoEnLaBBDD(Exception):
    pass


@dataclass(frozen=True)
class PerfilAve:
    especie: str
    nombre: str
    familia: str
    orden: str
    habitat: str
    foto: str


@dataclass(frozen=True)
class PerfilUsuario(UserMixin):
    username: str
    contrasena: str
    nombre: str
    apellido: str
    fecha_nacimiento: str
    ocupacion: str
    nacionalidad: str
    email: str
    dir_foto: str
    
    def get_id(self):
        return self.username
    
    
def obtener_todas_las_fotos_de_aves():
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM aves.foto_ave;
            """)

            fotos_de_aves = cursor.fetchall()

        connection.commit()

    fotos_de_aves = [foto_de_ave[0] for foto_de_ave in fotos_de_aves]

    return fotos_de_aves



def obtener_id_avist():
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT MAX(id_avistamiento)
                FROM aves.avistamiento;
            """)

            avist = cursor.fetchall()

        connection.commit()
        print(int(avist[0][0]))
        return int(avist[0][0])

def obtener_informacion_ave(especie: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT * FROM aves.ave WHERE especie='{especie}';
            """)

            informacion_aves = cursor.fetchall()

        connection.commit()
        return informacion_aves


def obtener_perfil_ave(especie: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (a.especie, a.nombre, a.orden, a.familia, a.habitat, sujetos.dir_foto)
            FROM aves.ave as a, aves.sujeto as sujetos 
            WHERE a.especie='{especie}'
            AND a.especie = sujetos.especie;
            """)

            informacion_ave = cursor.fetchall()

            try:
                informacion_ave = informacion_ave[0][0]
            except IndexError:
                raise NoEncontradoEnLaBBDD("Ave no encontrada")

            connection.commit()

            return PerfilAve(*informacion_ave)

def obtener_ingreso_usuario(username: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (
                u.username,
                u.contrasena,
                u.nombre_usuar,
                u.apellido,
                u.fecha_nacimiento,
                u.ocupacion,
                u.nacionalidad,
                u.email,
                u.dir_foto_usr
            )
            FROM aves.usuario as u
            WHERE u.username='{username}'
            """)

            perfil_usuario_tupla = cursor.fetchall()

            try:
                perfil_usuario_tupla = perfil_usuario_tupla[0][0]
            except IndexError:
                raise NoEncontradoEnLaBBDD("Usuario no Encontrado")

            connection.commit()

            return PerfilUsuario(*perfil_usuario_tupla)

def obtener_perfil_usuario(username: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (
                u.username,
                u.contrasena,
                u.nombre_usuar,
                u.apellido,
                u.fecha_nacimiento,
                u.ocupacion,
                u.nacionalidad,
                u.email,
                u.dir_foto_usr
            )
            FROM aves.usuario as u
            WHERE u.username='{username}'
            """)

            perfil_usuario_tupla = cursor.fetchall()

            try:
                perfil_usuario_tupla = perfil_usuario_tupla[0][0]
            except IndexError:
                raise NoEncontradoEnLaBBDD("Usuario no Encontrado")

            connection.commit()

            return PerfilUsuario(*perfil_usuario_tupla)

@dataclass(frozen=True)
class NuevoUsuario:
    username: str
    contrasena: str
    nombre: str
    apellido: str
    fecha_nacimiento: str
    ocupacion: str
    nacionalidad: str
    email: str
    dir_foto: str
    
    
def comprobar_usuario(username:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (
                u.username
            )
            FROM aves.usuario as u
            WHERE u.username='{username}'
            """)

            perfil_usuario_tupla = cursor.fetchall()

            try:
                perfil_usuario_tupla = perfil_usuario_tupla[0][0]
            except IndexError:
                connection.commit()

                return True
                

            connection.commit()

            return False
    
    
def hecho_por(username: str, idav: int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.hecho_por VALUES ('{username}',{idav})   
            """)

    
def ingresar_usuario(username: str, contrasena: str, nombre: str, apellido: str, fecha_nacimiento: str, ocupacion: str, nacionalidad: str, email: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.usuario VALUES ('{username}','{contrasena}','{nombre}','{apellido}','{fecha_nacimiento}','{ocupacion}','{nacionalidad}','{email}','https://static.wikia.nocookie.net/yugioh/images/5/59/TheWingedDragonofRa-TF06-JP-VG.png')   
            """)

        
def obtener_todas_las_fotos_de_un_ave(especie: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT dir_foto FROM aves.sujeto WHERE especie='{especie}';
            """)

            fotos_ave_tuplas = cursor.fetchall()

            connection.commit()

            fotos_ave = [foto_ave[0] for foto_ave in fotos_ave_tuplas]

            try:
                return fotos_ave
            except IndexError:
                return NoEncontradoEnLaBBDD(f"Ave {especie} no tiene fotos.")

@dataclass(frozen=True)
class AvistamientoUsuario:
    estado: str
    nido: bool
    sexo: str
    estado_conservacion: str
    fecha_y_hora: str


def obtener_todos_los_avistamientos_de_un_usuario(username: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (
                avistamiento.estado,
                avistamiento.nido,
                avistamiento.sexo,
                avistamiento.estado_conservacion,
                cuando.fecha_hora
            ) 
            FROM aves.avistamiento as avistamiento, aves.cuando as cuando, aves.hecho_por as hecho_por
            WHERE hecho_por.username='{username}'
            AND hecho_por.id_avistamiento = avistamiento.id_avistamiento
            AND avistamiento.id_avistamiento = cuando.id_avistamiento;
            """)

            avistamientos_tupla = [avistamientos_tupla[0] for avistamientos_tupla in cursor.fetchall()]

            avistamientos = []

            for avistamiento_tupla in avistamientos_tupla:
                avistamientos.append(AvistamientoUsuario(
                    estado=avistamiento_tupla[0],
                    nido=avistamiento_tupla[1] == 'f',
                    sexo=avistamiento_tupla[2].capitalize(),
                    estado_conservacion=avistamiento_tupla[3].capitalize(),
                    fecha_y_hora=avistamiento_tupla[4]
                ))

            connection.commit()

            return avistamientos

def asignar_avistamiento_usuario(username:str,avistamiento:int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.hecho_por VALUES ('{username}',{avistamiento})   
            """)

#Falta obtener el id del avistamiento    
def ingresar_avistamiento(iden:int, estado:str,nido:bool,sexo:str,estado_cons:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.avistamiento VALUES ({iden},'{estado}','{nido}','{sexo}',FALSE,'{estado_cons}')   
            """)

#def ingresar_comp_obs():
    
    
#def ingresar_apar_obs():

if __name__ == "__main__":
    print(obtener_perfil_ave('Phoebastria irrorata'))
    print(obtener_perfil_usuario("lazyostrich760"))

    for avistamiento in obtener_todos_los_avistamientos_de_un_usuario('lazyostrich760'):
        print(avistamiento)
