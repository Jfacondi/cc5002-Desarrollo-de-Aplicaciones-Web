T2

Se implemento todo lo solicitado
Se hizo uso de redirect y flash para el aviso de un registro exitoso
Se implemento manejo basico de errores tanto al momento de intentar ver la informacion artesano
de un artesano inexistente en la base de datos como al momento de intentar ingresar a una pagina
que no esta definida redirigiendo en ambos casos a una pagina de error, pero cambiando
el error segun el caso.
Todas las consultas SQL se encuentran en el archivo database/db.py
Al momento de apretar la primera confirmacion en el formulario se activa la validacion
de javascript, si esta es correcta se manda a una confirmacion en donde si es confirmado
el registro se manda a la base de datos mediante flask y se realiza una segunda validacion 
en el servidor, si esta es correcta se redirige a la pagina de inicio, si no se redirige
nuevamente al formulario mostrando los errores correspondientes.

## Hay varias librerias que se descargaron sin querer y no se usaron, pero no se eliminaron por si acaso.
## Tambien notar que el numero es formato +(xxx)xxxxxxxxx

T3

Se implemento todo lo solicitado
Se hizo uso de ajax para los graficos, ademas de la libreria highcharts
se implemento el mismo manejo de errores usado para los artesanos en tablas/informacion/registro de hinchas 
Se implementa en la navbar la seccion de estadisticas que permite ver los graficos, ademas de un boton para alternar los mismos
