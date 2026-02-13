from flask import Flask, render_template, request, redirect, url_for
from c_herrajes import calcular_herrajes


app = Flask(__name__)

# Importar Blueprints de los módulos de funcionalidad
from resortes import resortes_blueprint

# Registrar Blueprints

app.register_blueprint(resortes_blueprint, url_prefix='/resortes')




# Definición de rutas y vistas en Flask
@app.route('/')
def inicio():
    # Ruta para la página de inicio. Carga 'inicio.html'.
    return render_template('inicio.html')

@app.route('/generar') 
def generar():
    # Ruta para la página de Generador de Herrajes. Carga 'GHerrajes.html'.
    return render_template('GHerrajes.html')

from g_rieles import calcular_rieles

@app.route('/rieles', methods=['GET', 'POST'])
def rieles():
    resultado = None  # Inicializa resultado como None

    if request.method == 'POST':
        # Obtiene los valores del formulario
        cantidad_paneles_46cm = int(request.form['cantidad_paneles_46cm'])
        cantidad_paneles_53cm = int(request.form['cantidad_paneles_53cm'])

        # Llama a la función de cálculo con los datos del formulario
        resultado = calcular_rieles(cantidad_paneles_46cm, cantidad_paneles_53cm)

    # Renderiza nuevamente 'rieles.html' y pasa el resultado
    return render_template('rieles.html', resultado=resultado)

from g_chicote import asignar_chicote
@app.route('/chicote', methods=['GET', 'POST'])
def g_chicote():
    longitud_chicote = None  # Inicializa la variable con None
    if request.method == 'POST':
        altura = float(request.form['alto'])
        longitud_chicote = asignar_chicote(altura)
    # Pasa 'longitud_chicote' a la plantilla, será None en GET y tendrá valor en POST
    return render_template('chicote.html', longitud_chicote=longitud_chicote)

#------------Aquí inicia el calculo de los herrajes------------------------------------
@app.route('/calcular', methods=['POST'])
def calcular():
    # Obtener los valores del formulario
    # ancho = float(request.form['ancho'])
    # alto = float(request.form['alto'])

#------------Agregado 06/01/2026------------------------------------
    ancho = float(request.form.get('ancho'))
    alto = float(request.form.get('alto'))
    tipo_porton = request.form.get('tipo_porton')
    peso_form = request.form.get('peso')
#-------------------------------------------------------------------
    if tipo_porton == 'spazi':
        peso_objetivo = ancho * alto * 10.5
    else:
        peso_objetivo = float(peso_form)
#------------Agregado 06/01/2026------------------------------------
    # Calcular los herrajes
    #resultado = calcular_herrajes(ancho, alto)
    resultado = calcular_herrajes(ancho, alto, peso_objetivo, tipo_porton)

    # --------Aquí termina el calclo de los herrajes-------------

#------------ CÁLCULO DE RIELES Y CHICOTES ------------------
    # --------Aquí inicia el calculo de los rieles---------------
    from g_rieles import calcular_rieles

    texto_paneles = resultado['paneles']  # Ej: "0 paneles de 46cm y 4 paneles de 53cm"
    cant_46 = 0
    cant_53 = 0

    for parte in texto_paneles.split(" y "):
        cantidad = int(parte.split(" ")[0])
        if "46" in parte:
            cant_46 = cantidad
        elif "53" in parte:
            cant_53 = cantidad

    # Calcular rieles
    rieles = calcular_rieles(cant_46, cant_53)
    # --------Aquí termina el calclo de los rieles-------------


    # ---------Aquí inicia el calculo del chicote --------------
    from g_chicote import asignar_chicote
    chicote_resultado = asignar_chicote(alto)

    if isinstance(chicote_resultado, (float, int)):
        resultado['chicote'] = f"Un par de chicotes de {chicote_resultado} mts"
    else:
        resultado['chicote'] = chicote_resultado
    # ---------- Aquí termina el calculo de chicotes -----------

    # Enviar todo al HTML

    # return render_template(
    #     'resultado_herrajes.html',
    #     ancho=ancho,
    #     alto=alto,
    #     resultado=resultado,
    #     rieles=rieles,
    #     chicote=resultado['chicote']  #  enviamos explícitamente también el chicote
    # )
    return render_template(
    'resultado_herrajes.html',
    ancho=ancho,
    alto=alto,
    resultado=resultado,
    rieles=rieles,
    chicote=resultado['chicote'],
    opciones_resortes=resultado.get('opciones_resortes', [])
    )

#----------Aquí termina el bloque que agrega el cálculo de los rieles y del chicote-------------------


if __name__ == '__main__':
    app.run(debug=True)
