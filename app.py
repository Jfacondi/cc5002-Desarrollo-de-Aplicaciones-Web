from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import cross_origin
from utils.validations import *
from database import db
import math
import filetype
import hashlib
import os
from werkzeug.utils import secure_filename
import uuid
import cryptography
UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)


app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/ver-hinchas", defaults={'page': 1})
@app.route("/ver-hinchas/<int:page>")
def ver_hinchas(page):
    total_rows = db.get_hincha_rows_count()
    page_size = 5
    total_page = math.ceil(total_rows / page_size)
    next = page + 1
    prev = page - 1
    data=[]
    for hincha in db.get_hinchas((page-1)*page_size):
        id_h , comuna , transporte , nombre , email , celular , descripcion = hincha
        comunas = db.get_comuna_nombre(comuna)[0]
        sports = db.get_hincha_sports(id_h)
        sports_hincha = [db.get_sport_nombre(sport[0])[0] for sport in sports]
        data.append({
            "comuna": comunas,
            "nombre": nombre,
            "telefono": celular,
            "transporte": transporte,
            "descripcion": descripcion,
            "email": email,
            "id": id_h,
            "sports": ", ".join(sports_hincha),
        })
    return render_template("ver-hinchas.html", hinchas=data, page=total_page, next=next, prev=prev)

@app.route('/ver_artesanos', defaults={'page': 1})
@app.route('/ver_artesanos/<int:page>')
def ver_artesanos(page):
    total_rows = db.get_rows_count()
    page_size = 5
    total_page = math.ceil(total_rows / page_size)
    next = page + 1
    prev = page - 1

    #database manipulation here
    data=[]
    for artesano in db.get_artesanos((page-1)*page_size):
        id_a , comuna , _ , nombre , _ , celular = artesano
        comunas = db.get_comuna_nombre(comuna)[0]
        tipos = db.get_tipos_artesano(id_a)
        tipos_artesanias = [db.get_categoria_nombre(tipo[0])[0] for tipo in tipos]
        fotos= db.get_fotos(id_a)
        _filenames = [foto[0] for foto in fotos]
        img_filenames = [f"uploads/{_filename}" for _filename in _filenames]
        path_images= [url_for('static', filename=img_filename) for img_filename in img_filenames]
        data.append({
            "comuna": comunas,
            "nombre": nombre,
            "telefono": celular,
            "tipo_artesanias": ", ".join(tipos_artesanias),
            "id": id_a,
            "path_images": path_images
        })
    return render_template('ver-artesanos.html', artesanos=data, page=total_page, next=next, prev=prev)

@app.route('/informacion_hincha/<int:id>')
def informacion_hincha(id):
    ids= db.get_hincha_ids()
    bandera= False
    for id_a in ids:
        if id == id_a[0]:
            bandera= True
    if bandera == False:
        flash('El Hincha no existe', 'error')
        return redirect(url_for('error'))
    else:
        data=[]
        hincha = db.get_hincha(id)
        id_h , comuna , transporte , nombre , email , celular , descripcion = hincha
        comunas = db.get_comuna_nombre(comuna)[0]
        sports = db.get_hincha_sports(id_h)
        sports_hincha = [db.get_sport_nombre(sport[0])[0] for sport in sports]
        region_id= db.get_region_nombre(comuna)[0]
        region = db.get_region_by_id(region_id)[0]
        data.append({
            "region": region,
            "comuna": comunas,
            "nombre": nombre,
            "telefono": celular,
            "transporte": transporte,
            "descripcion": descripcion,
            "email": email,
            "id": id_h,
            "sports": ", ".join(sports_hincha),
        })
        return render_template('informacion-hinchas.html', hinchas=data)


@app.route('/informacion_artesano/<int:id>')
def informacion_artesano(id):
    ids= db.get_artesano_ids()
    bandera= False
    for id_a in ids:
        if id == id_a[0]:
            bandera= True
    if bandera == False:
        flash('El artesano no existe', 'error')
        return redirect(url_for('error'))
    else:
        data=[]
        artesano = db.get_artesano(id)
        id_a , comuna , descripcion , nombre , email , celular = artesano
        comunas = db.get_comuna_nombre(comuna)[0]
        tipos = db.get_tipos_artesano(id_a)
        tipos_artesanias = [db.get_categoria_nombre(tipo[0])[0] for tipo in tipos]
        fotos= db.get_fotos(id_a)
        _filenames = [foto[0] for foto in fotos]
        region = db.get_region_nombre(comuna)[0]
        region = db.get_region_by_id(region)[0]
        img_filenames = [f"uploads/{_filename}" for _filename in _filenames]
        path_images= [url_for('static', filename=img_filename) for img_filename in img_filenames]
        data.append({
            "region": region,
            "comuna": comunas,
            "nombre": nombre,
            "telefono": celular,
            "tipo_artesanias": ", ".join(tipos_artesanias),
            "descripcion": descripcion,
            "email": email,
            "id": id_a,
            "path_images": path_images
        })
        return render_template('informacion-artesano.html', artesanos=data)



@app.route('/agregar_hincha', methods=['GET','POST'])
def agregar_hincha():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        transporte = request.form.get('transporte')
        comuna = request.form.get('comuna')
        region = request.form.get('region')
        sports = request.form.getlist('sports')
        descripcion = request.form['descripcion']
        if transporte == None:
            transporte = "No"
        if comuna == None:
            comuna = "No"
        if region == None:
            region = "No"
        error = ""
        if(validate_hincha(nombre, email, telefono, transporte, comuna, region, sports, descripcion)[0]== True):
            status, msg = db.registrar_hincha(comuna, transporte, nombre, email, telefono, descripcion, sports)
            if status:
                flash('Hincha registrado correctamente', 'success')
                return redirect(url_for('index'))
            error = msg
        else:
            error = "Error en los datos ingresados "
            error = error + validate_hincha(nombre, email, telefono, transporte, comuna, region, sports, descripcion)[1]
            error = error + db.validate_comuna(comuna,region)[1]
        return render_template('agregar-hincha.html', error=error)


    return render_template('agregar-hincha.html')



@app.route('/agregar_artesano', methods=['GET', 'POST'])
def agregar_artesano():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        comuna = request.form.get('comuna')
        region = request.form.get('region')
        artesania = request.form.getlist('sports')
        foto1 = request.files['foto-1']
        foto2 = request.files['foto-2']
        foto3 = request.files['foto-3']
        descripcion = request.form['descripcion']
        if comuna == None:
            comuna = "No"
        if region == None:
            region = "No"
        error = ""
        if (validate_artesano(nombre,email,telefono,comuna,region,artesania, descripcion)[0]== True) and ((validate_fotos(foto1) == True) or (validate_fotos(foto2) == True) or (validate_fotos(foto3) == True)):
            status, msg = db.registrar_artesano(comuna,descripcion,nombre,email,telefono,artesania)
            id = db.get_artesano_id(nombre)[0]
            if(validate_fotos(foto1) == True):
                _filename = hashlib.sha256(
                    secure_filename(foto1.filename).encode('utf-8')).hexdigest()
                _extension = filetype.guess(foto1).extension
                img_filename = f"{_filename}.{_extension}"

                foto1.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
                db.registrar_foto(app.config['UPLOAD_FOLDER'],img_filename, id)
            if(validate_fotos(foto2) == True):
                _filename = hashlib.sha256(
                    secure_filename(foto2.filename).encode('utf-8')).hexdigest()
                _extension = filetype.guess(foto2).extension
                img_filename = f"{_filename}.{_extension}"

                foto2.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
                db.registrar_foto(app.config['UPLOAD_FOLDER'],img_filename, id)
            if(validate_fotos(foto3) == True):
                _filename = hashlib.sha256(
                    secure_filename(foto3.filename).encode('utf-8')).hexdigest()
                _extension = filetype.guess(foto3).extension
                img_filename = f"{_filename}.{_extension}"
                foto3.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
                db.registrar_foto(app.config['UPLOAD_FOLDER'],img_filename, id)
            if status:
                flash('Artesano registrado correctamente', 'success')
                return redirect(url_for('index'))
            error = msg
        else:
            error = "Error en los datos ingresados "
            error = error + validate_artesano(nombre,email,telefono,comuna,region,artesania, descripcion)[1]
            error = error + db.validate_comuna(comuna,region)[1]
        return render_template('agregar-artesano.html', error=error)
            
    else:
        return render_template('agregar-artesano.html')

#rutas estadisticas API
@app.route("/estadisticas")
def estadisticas():
    return render_template("estadisticas.html")

@app.route("/get_estadisticas", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_estadisticas():
    hinchas = [{
        "tipo": db.get_sport_nombre(id)[0],
        "cantidad": db.get_estadisticas_hinchas(id)[0]
    } for id, tipo in db.get_sports() if db.get_estadisticas_hinchas(id)[0] != 0]

    artesanos = [{
        "tipo": db.get_categoria_nombre(id)[0],
        "cantidad": db.get_estadisticas_artesanos(id)[0]
    } for id, tipo in db.get_tipos() if db.get_estadisticas_artesanos(id)[0] != 0]
    
    return jsonify({
        "hinchas": hinchas,
        "artesanos": artesanos
    })


@app.route('/exito')
def exito():
    return render_template('exito.html')
@app.route('/error')
def error():
    return render_template('error.html')
@app.errorhandler(404)
def page_not_found(e):
    flash('Error 404', 'error')
    flash('Pagina no encontrada', 'error')
    return redirect(url_for('error'))
if __name__ == '__main__':
    app.run(port=3006, debug=True)

