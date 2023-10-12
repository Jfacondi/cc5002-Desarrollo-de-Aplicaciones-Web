-- artesano
-- insertar
INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (?,?,?,?,?)
-- obtener listado de artesanos ordenados desde el mas reciente insertado al más antiguo
SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano ORDER BY id DESC
-- obtener listado de artesanos ordenados desde el mas reciente insertado al más antiguo limitado
-- a los primeros 5
SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano ORDER BY id DESC LIMIT 0, 5
-- idem anterior, pero los siguientes 5 (siguiente página)
SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano ORDER BY id DESC LIMIT 5, 5
-- idem anterior pero obteniendo el nombre de comuna en lugar de ID
SELECT artesano.id, comuna.nombre, descripcion_artesania, artesano.nombre, email, celular FROM artesano, comuna WHERE artesano.comuna_id=comuna.id ORDER BY id DESC LIMIT 5, 5

-- artesano_tipo
-- insertar
INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (?,?)
-- obtener los tipos de artesanias de un artesano en particular
SELECT TA.nombre FROM tipo_artesania TA, artesano_tipo AT WHERE AT.tipo_artesania_id=TA.id AND AT.artesano_id=?

-- foto
-- insertar
INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (?,?,?)
-- obtener fotos informadas por un artesano
SELECT ruta_archivo, nombre_archivo FROM foto WHERE artesano_id=?

-- obtener el último id insertado
SELECT LAST_INSERT_ID()

