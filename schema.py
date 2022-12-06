import psycopg
from dataclasses import dataclass
from flask_login import UserMixin
from psycopg.rows import class_row

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


@dataclass(frozen=True)
class TarjetaUsuario:
    username: str
    nombre: str
    apellido: str
    ocupacion: str
    n_avistamientos: int

@dataclass(frozen=True)
class TarjetaUsuario:
    username: str
    nombre: str
    apellido: str
    ocupacion: str
    n_avistamientos: int


class TarjetaAvistamientoDeAve():
    dir_foto: str
    nombre_ave: str
    especie_ave: str
    fecha_y_hora: str
    nombre_ubicacion: str
    region_ubicacion: str


def eliminar_usuario(username: str):
    query = """
    DELETE FROM aves.usuario WHERE username = %s;
    """

    (psycopg.connect(conninfo=CONN_STRING).execute(query, (username,)).connection.commit())



def obtener_todos_los_avistamientos():
    query = """
    SELECT foto_ave.dir_foto as "dir_foto",
       ave.nombre as "nombre_ave",
       ave.especie as "especie_ave",
       fecha_y_hora.fecha_hora as "fecha_y_hora",
       ubicacion.nombre as "nombre_ubicacion",
       ubicacion.region as "region_ubicacion"
    FROM aves.avistamiento as avistamiento,

         aves.avistado as avistado,
         aves.ave as ave,

         aves.visto_en as visto_en,
         aves.ubicacion as ubicacion,

         aves.cuando as cuando,
         aves.fecha_y_hora as fecha_y_hora,
         aves.avistado_en as avistado_en,
         aves.foto_ave as foto_ave
    WHERE avistamiento.id_avistamiento = avistado.id_avistamiento
      AND avistado.especie = ave.especie

      AND avistamiento.id_avistamiento = visto_en.id_avistamiento
      AND visto_en.nombre = ubicacion.nombre

      AND avistamiento.id_avistamiento = cuando.id_avistamiento
      AND cuando.fecha_hora = fecha_y_hora.fecha_hora

      AND avistamiento.id_avistamiento = avistado_en.id_avistamiento
      AND avistado_en.dir_foto = foto_ave.dir_foto
    """

    avistamientos = (psycopg.connect(conninfo=CONN_STRING, row_factory=class_row(TarjetaAvistamientoDeAve))
                     .execute(query).fetchall())

    return avistamientos


def obtener_todos_los_avistamientos_de_un_ave(especie_ave: str):
    query = """
    SELECT foto_ave.dir_foto as "dir_foto",
       ave.nombre as "nombre_ave",
       ave.especie as "especie_ave",
       fecha_y_hora.fecha_hora as "fecha_y_hora",
       ubicacion.nombre as "nombre_ubicacion",
       ubicacion.region as "region_ubicacion"
    FROM aves.avistamiento as avistamiento,

         aves.avistado as avistado,
         aves.ave as ave,

         aves.visto_en as visto_en,
         aves.ubicacion as ubicacion,

         aves.cuando as cuando,
         aves.fecha_y_hora as fecha_y_hora,
         aves.avistado_en as avistado_en,
         aves.foto_ave as foto_ave
    WHERE avistamiento.id_avistamiento = avistado.id_avistamiento
      AND avistado.especie = ave.especie

      AND avistamiento.id_avistamiento = visto_en.id_avistamiento
      AND visto_en.nombre = ubicacion.nombre

      AND avistamiento.id_avistamiento = cuando.id_avistamiento
      AND cuando.fecha_hora = fecha_y_hora.fecha_hora

      AND avistamiento.id_avistamiento = avistado_en.id_avistamiento
      AND avistado_en.dir_foto = foto_ave.dir_foto
      
      AND ave.especie = '%s';
    """

    avistamientos = (psycopg.connect(conninfo=CONN_STRING, row_factory=class_row(TarjetaAvistamientoDeAve))
                        .execute(query).fetchall(), especie_ave)

    return avistamientos


def obtener_todas_las_tarjetas_usuarios():
    query = """
    SELECT DISTINCT
        usr.username AS "username",
        usr.nombre_usuar AS "nombre",
        usr.apellido AS "apellido", usr.ocupacion AS "ocupacion",
        avistamientos_por_usuario.cuenta AS "n_avistamientos"
    FROM aves.usuario AS usr, (
    SELECT 
        username,
        count(id_avistamiento) AS cuenta 
        FROM aves.hecho_por 
        GROUP BY username
    ) as avistamientos_por_usuario
    WHERE avistamientos_por_usuario.username = usr.username;
    """

    tarjetas_usuario = (psycopg.connect(conninfo=CONN_STRING, row_factory=class_row(TarjetaUsuario))
                        .execute(query).fetchall())

    return tarjetas_usuario


def obtener_todas_las_tarjetas_aves():
    query = """
    SELECT 
        ave.especie as "especie",
        ave.nombre as "nombre",
        sujeto.dir_foto AS "foto",
        avistamientos_por_ave.cuenta AS "n_avistamientos"
    FROM aves.ave as ave, aves.sujeto as sujeto, (
    SELECT
        especie,
        count(id_avistamiento) AS cuenta 
        FROM aves.avistado 
        GROUP BY especie
    ) AS avistamientos_por_ave
    WHERE ave.especie = sujeto.especie
    AND avistamientos_por_ave.especie = ave.especie;
    """

    tarjetas_ave = (psycopg.connect(conninfo=CONN_STRING, row_factory=class_row(TarjetaUsuario))
                    .execute(query).fetchall())

    return tarjetas_ave

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
        return int(avist[0][0])
    
def obtener_id_apar():
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT MAX(id_apariencia_obs)
                FROM aves.apariencia_observada;
            """)

            avist = cursor.fetchall()

        connection.commit()
        return int(avist[0][0])
    
def obtener_id_comp():
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT MAX(id_comportamiento_obs)
                FROM aves.comportamiento_obsrvado;
            """)

            avist = cursor.fetchall()

        connection.commit()
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
            connection.commit()

    
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
    especie: str
    ubicacion: str


def obtener_todos_los_avistamientos_de_un_usuario(username: str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (
                avistamiento.estado,
                avistamiento.nido,
                avistamiento.sexo,
                avistamiento.estado_conservacion,
                cuando.fecha_hora,
                ave.especie,
                ubicacion.nombre
            ) 
            FROM aves.avistamiento as avistamiento, aves.cuando as cuando, aves.hecho_por as hecho_por, aves.ave as ave, aves.se_encuentra_en as se_encuentra_en, aves.avistado as avistado, aves.visto_en as visto_en
            WHERE hecho_por.username='{username}'
            AND hecho_por.id_avistamiento = avistamiento.id_avistamiento
            AND avistamiento.id_avistamiento = cuando.id_avistamiento
            AND avistamiento.id_avistamiento = avistado.id_avistamiento
            AND avistado.especie=ave.especie
            AND visto_en.id_avistamiento=id_avistamiento
            AND ubicacion.nombre=visto_en.nombre;
            """)

            avistamientos_tupla = [avistamientos_tupla[0] for avistamientos_tupla in cursor.fetchall()]

            avistamientos = []

            for avistamiento_tupla in avistamientos_tupla:
                avistamientos.append(AvistamientoUsuario(
                    estado=avistamiento_tupla[0],
                    nido=avistamiento_tupla[1] == 'f',
                    sexo=avistamiento_tupla[2].capitalize(),
                    estado_conservacion=avistamiento_tupla[3].capitalize(),
                    fecha_y_hora=avistamiento_tupla[4],
                    especie=avistamiento_tupla[5],
                    ubicacion=avistamiento_tupla[6]                    
                ))

            connection.commit()

            return avistamientos

def asignar_avistamiento_usuario(username:str,avistamiento:int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.hecho_por VALUES ('{username}',{avistamiento})   
            """)

def ingresar_avistamiento(iden:int, estado:str,nido:bool,sexo:str,estado_cons:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.avistamiento VALUES ({iden},'{estado}','{nido}','{sexo}',FALSE,'{estado_cons}')   
            """)
            connection.commit()

def ingresar_comp_obs(iden: int, alimentacion:str,nidificacion:str,migracion:bool,cronotipo:str,obs_ad:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.comportamiento_observado VALUES ({iden},'{alimentacion}','{nidificacion}',{migracion},'{cronotipo}','{obs_ad}')   
            """)
            
            connection.commit()

    
def ingresar_apar_obs(iden:str,tamano:str, alas:str, pico:str, patas:str, obs_ad:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.apariencia_observada VALUES ({iden},'{tamano}','{alas}',{pico},'{patas}','{obs_ad}')   
            """)
            
            connection.commit()
            
def avistamiento_especie(especie: str, avistamiento:int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.avistado VALUES ('{especie}',{avistamiento})   
            """)
            
            connection.commit()

def comprobar_ubicacion(nombre:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (
                f.nombre
            )
            FROM aves.ubicacion as f
            WHERE f.nombre='{nombre}'
            """)

            perfil_usuario_tupla = cursor.fetchall()

            try:
                perfil_usuario_tupla = perfil_usuario_tupla[0][0]
            except IndexError:
                connection.commit()

                return True
                

            connection.commit()

            return False
        
def registrar_ubicacion(nombre:str,tipo_localidad:str,region:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:          
            cursor.execute(f"""
            INSERT INTO aves.ubicacion VALUES ('{nombre}','{tipo_localidad}','{region}')   
            """)
            
            connection.commit()

def visto_en(ubicacion: str, tipo_localidad:str, region:str, avistamiento:int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            
            if comprobar_ubicacion(ubicacion):
                registrar_ubicacion(ubicacion)
                
            cursor.execute(f"""
            INSERT INTO aves.visto_en VALUES ('{ubicacion}',{avistamiento})   
            """)
            
            connection.commit()
            
def que_hacia(avistamiento:int,id_comp: int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.que_hacia VALUES ({avistamiento},{id_comp})   
            """)
            
            connection.commit()
            
def como_lucia(avistamiento:int,id_ap: int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.como_lucia VALUES ({avistamiento},{id_ap})   
            """)
            
            connection.commit()
            
def se_encuentra_en(especie: str, nombre:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO aves.se_encuentra_en VALUES ('{especie}','{nombre}')   
            """)
            
            connection.commit()
            
def comprobar_fecha(fecha:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT (
                f.fecha_hora
            )
            FROM aves.fecha_y_hora as f
            WHERE f.fecha_hora='{fecha}'
            """)

            perfil_usuario_tupla = cursor.fetchall()

            try:
                perfil_usuario_tupla = perfil_usuario_tupla[0][0]
            except IndexError:
                connection.commit()

                return True
                

            connection.commit()

            return False
        
def registrar_fecha(fecha:str):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:          
            cursor.execute(f"""
            INSERT INTO aves.fecha_y_hora VALUES ('{fecha}')   
            """)
            
            connection.commit()
    
        
def cuando(fecha: str, avistamiento:int):
    with psycopg.connect(conninfo=CONN_STRING) as connection:
        with connection.cursor() as cursor:
            
            if comprobar_fecha(fecha):
                registrar_fecha(fecha)
            
            cursor.execute(f"""
            INSERT INTO aves.cuando VALUES ('{fecha}',{avistamiento})   
            """)
            
            connection.commit()




if __name__ == "__main__":
    print(obtener_perfil_ave('Phoebastria irrorata'))
    print(obtener_perfil_usuario("lazyostrich760"))

    for avistamiento in obtener_todos_los_avistamientos_de_un_usuario('lazyostrich760'):
        print(avistamiento)
