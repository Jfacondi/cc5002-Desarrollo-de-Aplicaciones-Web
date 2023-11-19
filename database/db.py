import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn
def get_categoria_nombre(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM tipo_artesania WHERE id=%s;", (id,))
    nombre = cursor.fetchone()
    return nombre
def get_rows_count():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM artesano;")
    count = cursor.fetchone()
    return count[0]
def get_region_nombre(comuna):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT region_id FROM comuna WHERE id=%s;", (comuna,))
    region = cursor.fetchone()
    return region

def get_region_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM region WHERE id=%s;", (id,))
    region = cursor.fetchone()
    return region
def get_tipos():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM tipo_artesania;")
    tipos = cursor.fetchall()
    return tipos

def get_tipos_artesano(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo_artesania_id FROM artesano_tipo WHERE artesano_id=%s;", (id,))
    tipos = cursor.fetchall()
    return tipos
def get_artesanos(page_size):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano ORDER BY id DESC LIMIT %s, 5;", (page_size,))
    artesanos = cursor.fetchall()
    return artesanos
    
def get_artesano_id(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM artesano WHERE nombre=%s;", (nombre,))
    id = cursor.fetchone()
    return id
    
def get_artesano(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano WHERE id=%s;", (id,))
    artesano = cursor.fetchone()
    return artesano

def get_comuna_nombre(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM comuna WHERE id=%s;", (id,))
    nombre = cursor.fetchone()
    return nombre
def get_fotos(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_archivo FROM foto WHERE artesano_id=%s;", (id,))
    fotos = cursor.fetchall()
    return fotos
def create_artesano(comuna,descripcion,nombre,email,celular):
    conn = get_conn()
    cursor = conn.cursor()
    id = get_artesano_id(nombre)
    cursor.execute("INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (%s, %s, %s, %s, %s);", (comuna, descripcion, nombre, email, celular,))
    conn.commit()

def validate_comuna(value, value2):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM comuna WHERE id=%s AND region_id=%s;", (value, value2,))
    nombre = cursor.fetchone()
    if nombre is None:
        return False, "Comuna no corresponde a la region"
    else:
        return True, ""
def get_artesano_ids():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM artesano;")
    id = cursor.fetchall()
    return id
def create_artesano_tipo(nombre,tipos):
    conn = get_conn()
    cursor = conn.cursor()
    id= get_artesano_id(nombre)
    for tipo in tipos:
        cursor.execute("INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (%s, %s);" , (id,tipo))
    conn.commit()

def registrar_foto(foto_ruta, foto_nombre, id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (%s, %s, %s);", (foto_ruta, foto_nombre, id,))
    conn.commit()

def registrar_artesano(comuna,descripcion,nombre,email,celular,tipos):
    if get_artesano_id(nombre) is not None:
        return  False, "El artesano ya existe!!!!!"

    create_artesano(comuna,descripcion,nombre,email,celular)
    create_artesano_tipo(nombre,tipos)
    return True, "artesano registrado exitosamente"
# SEGUNDA PARTE
def get_sports():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM deporte;")
    sports = cursor.fetchall()
    return sports
def get_hincha_ids():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM hincha;")
    id = cursor.fetchall()
    return id
def get_hincha_rows_count():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hincha;")
    count = cursor.fetchone()
    return count[0]
def get_hinchas(page_size):
    conn=get_conn()
    cursor=conn.cursor()
    cursor.execute("SELECT id, comuna_id, modo_transporte, nombre, email, celular, comentarios FROM hincha ORDER BY id DESC LIMIT %s, 5;", (page_size,))
    hinchas=cursor.fetchall()
    return hinchas
def get_hincha_sports(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT deporte_id FROM hincha_deporte WHERE hincha_id=%s;", (id,))
    tipos = cursor.fetchall()
    return tipos
def get_hincha(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, comuna_id, modo_transporte, nombre, email, celular, comentarios FROM hincha WHERE id=%s;", (id,))
    hincha = cursor.fetchone()
    return hincha

def get_hincha_id(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM hincha WHERE nombre=%s;", (nombre,))
    id = cursor.fetchone()
    return id
def get_hincha_sports(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT deporte_id FROM hincha_deporte WHERE hincha_id=%s;", (id,))
    tipos = cursor.fetchall()
    return tipos
def get_sport_nombre(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM deporte WHERE id=%s;", (id,))
    nombre = cursor.fetchone()
    return nombre
def create_hincha(comuna, transporte, nombre, email, celular, comentario):
    conn = get_conn()
    cursor = conn.cursor()
    id = get_hincha_id(nombre)
    cursor.execute("INSERT INTO hincha (comuna_id, modo_transporte, nombre, email, celular, comentarios) VALUES (%s, %s, %s, %s, %s, %s);", (comuna, transporte, nombre, email, celular, comentario,))
    conn.commit()
def create_hincha_deportes(nombre,tipos):
    conn = get_conn()
    cursor = conn.cursor()
    id= get_hincha_id(nombre)
    for tipo in tipos:
        cursor.execute("INSERT INTO hincha_deporte (hincha_id, deporte_id) VALUES (%s, %s);" , (id,tipo))
    conn.commit()
def get_estadisticas_hinchas(id):
    conn= get_conn()
    cursor= conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hincha_deporte WHERE deporte_id=%s;", (id,))
    count=cursor.fetchone()
    return count
def get_estadisticas_artesanos(id):
    conn= get_conn()
    cursor= conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM artesano_tipo WHERE tipo_artesania_id=%s;", (id,))
    count=cursor.fetchone()
    return count

def registrar_hincha(comuna, transporte, nombre, email, celular, comentario, tipos):
    if get_hincha_id(nombre) is not None:
        return False, "El hincha ya existe!!!!!"
    create_hincha(comuna, transporte, nombre, email, celular, comentario)
    create_hincha_deportes(nombre, tipos)
    return  True, "hincha registrado exitosamente"
