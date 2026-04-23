from flask import Flask, render_template, request, redirect, url_for
from c_herrajes import calcular_herrajes

app = Flask(__name__)

from resortes import resortes_blueprint
app.register_blueprint(resortes_blueprint, url_prefix='/resortes')

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/generar') 
def generar():
    return render_template('GHerrajes.html')

from g_rieles import calcular_rieles

@app.route('/rieles', methods=['GET', 'POST'])
def rieles():
    resultado = None

    if request.method == 'POST':
        cantidad_paneles_46cm = int(request.form['cantidad_paneles_46cm'])
        cantidad_paneles_53cm = int(request.form['cantidad_paneles_53cm'])
        resultado = calcular_rieles(cantidad_paneles_46cm, cantidad_paneles_53cm)

    return render_template('rieles.html', resultado=resultado)

from g_chicote import asignar_chicote

@app.route('/chicote', methods=['GET', 'POST'])
def g_chicote():
    longitud_chicote = None
    if request.method == 'POST':
        altura = float(request.form['alto'])
        longitud_chicote = asignar_chicote(altura)

    return render_template('chicote.html', longitud_chicote=longitud_chicote)

# ================= HERREAJES =================
@app.route('/calcular', methods=['POST'])
def calcular():

    ancho = float(request.form.get('ancho'))
    alto = float(request.form.get('alto'))
    tipo_porton = request.form.get('tipo_porton')
    peso_form = request.form.get('peso')

    # 👉 Solo para genérico
    if tipo_porton == 'generico':
        peso_objetivo = float(peso_form)
    else:
        peso_objetivo = 0  # placeholder, ya no usamos fórmula vieja

    # 👉 cálculo real
    resultado = calcular_herrajes(ancho, alto, peso_objetivo, tipo_porton)

    # 🔥 NUEVO: obtener peso real desde herrajes
    peso_real = resultado.get('peso_total', peso_objetivo)

    # ================= RIELES =================
    texto_paneles = resultado['paneles']
    cant_46 = 0
    cant_53 = 0

    for parte in texto_paneles.split(" y "):
        cantidad = int(parte.split(" ")[0])
        if "46" in parte:
            cant_46 = cantidad
        elif "53" in parte:
            cant_53 = cantidad

    rieles = calcular_rieles(cant_46, cant_53)

    # ================= CHICOTE =================
    chicote_resultado = asignar_chicote(alto)

    if isinstance(chicote_resultado, (float, int)):
        resultado['chicote'] = f"Un par de chicotes de {chicote_resultado} mts"
    else:
        resultado['chicote'] = chicote_resultado

    return render_template(
        'resultado_herrajes.html',
        ancho=ancho,
        alto=alto,
        peso_confirmacion=peso_real,  # 🔥 ya correcto
        resultado=resultado,
        rieles=rieles,
        chicote=resultado['chicote'],
        opciones_resortes=resultado.get('opciones_resortes', [])
    )

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)
