from flask import Flask, render_template, request, redirect, url_for

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

from c_herrajes import calcular_herrajes

@app.route('/calcular', methods=['POST'])
def calcular():
    # Obtener los valores del formulario
    ancho = float(request.form['ancho'])
    alto = float(request.form['alto'])

    # Calcular los herrajes
    resultado = calcular_herrajes(ancho, alto)

    # Enviar el resultado a la plantilla
    return render_template('resultado_herrajes.html', ancho=ancho, alto=alto, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)