import re
import filetype

def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if conf_img is None:
        return False

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validate_tipos(value):
    if len(value) == 0:
        return False
    if len(value) > 3:
        return False
    for tipo in value:
        if int(tipo) > 9 or int(tipo) < 1:
            return False
    return True

def validate_nombre(value):
    if len(value) == 0:
        return False
    if len(value) > 80:
        return False
    return True

def validate_email(value):
    if len(value) == 0:
        return False
    if len(value) > 80:
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
        return False
    return True

def validate_telefono(value):
    if len(value) == 0:
        return False
    if len(value) > 15:
        return False
    if not re.match(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", value):
        return False
    return True

def validate_comuna(value):
    if len(value) == 0:
        return False
    if int(value) < 10101 or int(value) > 130606:
        return False
    return True
def validate_region(value):
    if len(value) == 0:
        return False
    if int(value) < 1 or int(value) > 16:
        return False
    return True

def validate_descripcion(value):
    if len(value) > 300:
        return False
    return True

def validate_artesano(nombre,email,telefono,comuna,region,artesania,descripcion):
    if not validate_nombre(nombre):
        return False
    if not validate_email(email):
        return False
    if not validate_telefono(telefono):
        return False
    if not validate_comuna(comuna):
        return False
    if not validate_region(region):
        return False
    if not validate_tipos(artesania):
        return False
    if not validate_descripcion(descripcion):
        return False
    return True
def validate_fotos(foto):
    if validate_conf_img(foto):
        return True
    return False
