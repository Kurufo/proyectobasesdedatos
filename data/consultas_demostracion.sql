-- 1.- Obtener todas las aves

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


-- 2.- Todos los avistamientos de un ave
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

  AND ave.especie = 'Caranca';

-- 3.- Al consultar por el perfil del usuario...
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
WHERE u.username='yellowdog588';


-- 4.- FILTRO DE AVISTAMIENTOS POR SÖLO FECHA
SELECT DISTINCT avistado_en.dir_foto,
                ave.nombre,
                hecho_por.username,
                cuando.fecha_hora
FROM aves.avistamiento,
     aves.avistado_en,
     aves.avistado,
     aves.ave,
     aves.hecho_por,
     aves.cuando
WHERE avistado_en.id_avistamiento = avistamiento.id_avistamiento
  AND hecho_por.id_avistamiento = avistamiento.id_avistamiento
  AND avistado.especie = ave.especie
  AND avistado.id_avistamiento = avistamiento.id_avistamiento
  AND cuando.id_avistamiento = avistamiento.id_avistamiento
  AND cuando.fecha_hora < '2022-11-10 23:08:19.198405'::date;

-- 5.- Avistamientos por región
SELECT DISTINCT dir_foto,
                ave.nombre,
                hecho_por.username,
                ubicacion.region,
                ubicacion.nombre,
FROM aves.ubicacion,
     aves.visto_en,
     aves.avistamiento,
     aves.avistado_en,
     aves.avistado,
     aves.ave,
     aves.hecho_por
WHERE ubicacion.nombre=visto_en.nombre
  AND hecho_por.id_avistamiento = avistamiento.id_avistamiento
  AND avistado_en.id_avistamiento = avistamiento.id_avistamiento
  AND avistado.id_avistamiento = avistamiento.id_avistamiento
  AND visto_en.id_avistamiento = avistamiento.id_avistamiento
  AND avistado.especie = ave.especie
  AND ubicacion.region = 'Magallanes';

-- 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma 6.- Obtener todas las fotos en la plataforma
SELECT DISTINCT dir_foto FROM aves.foto_ave;

-- 7.- Múltiples filtros
SELECT DISTINCT dir_foto,
                ave.nombre,
                hecho_por.username,
                ubicacion.region,
                ubicacion.nombre,
                cuando.fecha_hora
FROM aves.ubicacion,
     aves.visto_en,
     aves.avistamiento,
     aves.avistado_en,
     aves.avistado,
     aves.ave,
     aves.hecho_por,
     aves.cuando
WHERE ubicacion.nombre=visto_en.nombre
  AND hecho_por.id_avistamiento = avistamiento.id_avistamiento
  AND avistado_en.id_avistamiento = avistamiento.id_avistamiento
  AND avistado.id_avistamiento = avistamiento.id_avistamiento
  AND visto_en.id_avistamiento = avistamiento.id_avistamiento
  AND cuando.id_avistamiento = avistamiento.id_avistamiento
  AND avistado.especie = ave.especie
  AND ubicacion.region = 'Magallanes'
  AND cuando.fecha_hora > '2022-08-14 23:10:08.283645'::date;

