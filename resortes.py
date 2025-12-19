from flask import Blueprint, request, render_template, jsonify
import itertools

# Crear Blueprint para resortes
resortes_blueprint = Blueprint('resortes', __name__, template_folder='templates')



# Datos de los resortes proporcionados 
resortes = [
    {'tipo': '9X7', 'vueltas': 5.5, 'peso_por_resorte': 24.4},
    {'tipo': '9X7', 'vueltas': 6, 'peso_por_resorte': 25.7},
    {'tipo': '9X7', 'vueltas': 6.5, 'peso_por_resorte': 26.9},
    {'tipo': '9X7', 'vueltas': 7, 'peso_por_resorte': 28.3},
    {'tipo': '9X7', 'vueltas': 7.5, 'peso_por_resorte': 29.7},
    {'tipo': '9X7', 'vueltas': 8, 'peso_por_resorte': 31.2},
    {'tipo': '9X7', 'vueltas': 8.5, 'peso_por_resorte': 32.8},

    {'tipo': '9X8', 'vueltas': 5.5, 'peso_por_resorte': 28.4},
    {'tipo': '9X8', 'vueltas': 6, 'peso_por_resorte': 29.8},
    {'tipo': '9X8', 'vueltas': 6.5, 'peso_por_resorte': 31.3},
    {'tipo': '9X8', 'vueltas': 7, 'peso_por_resorte': 32.9},
    {'tipo': '9X8', 'vueltas': 7.5, 'peso_por_resorte': 34.5},
    {'tipo': '9X8', 'vueltas': 8, 'peso_por_resorte': 36.3},
    {'tipo': '9X8', 'vueltas': 8.5, 'peso_por_resorte': 38.1},
    {'tipo': '9X8', 'vueltas': 9, 'peso_por_resorte': 40},
    {'tipo': '9X8', 'vueltas': 9.5, 'peso_por_resorte': 42},

    {'tipo': '10X7', 'vueltas': 5.5, 'peso_por_resorte': 27.2},
    {'tipo': '10X7', 'vueltas': 6, 'peso_por_resorte': 28.6},
    {'tipo': '10X7', 'vueltas': 6.5, 'peso_por_resorte': 30},
    {'tipo': '10X7', 'vueltas': 7, 'peso_por_resorte': 31.5},
    {'tipo': '10X7', 'vueltas': 7.5, 'peso_por_resorte': 33.1},
    {'tipo': '10X7', 'vueltas': 8, 'peso_por_resorte': 34.7},
    {'tipo': '10X7', 'vueltas': 8.5, 'peso_por_resorte': 36.5},

    {'tipo': '10X8', 'vueltas': 5.5, 'peso_por_resorte': 31.6},
    {'tipo': '10X8', 'vueltas': 6, 'peso_por_resorte': 33.2},
    {'tipo': '10X8', 'vueltas': 6.5, 'peso_por_resorte': 34.9},
    {'tipo': '10X8', 'vueltas': 7, 'peso_por_resorte': 36.6},
    {'tipo': '10X8', 'vueltas': 7.5, 'peso_por_resorte': 38.4},
    {'tipo': '10X8', 'vueltas': 8, 'peso_por_resorte': 40.4},
    {'tipo': '10X8', 'vueltas': 8.5, 'peso_por_resorte': 42.4},
    {'tipo': '10X8', 'vueltas': 9, 'peso_por_resorte': 44.5},
    {'tipo': '10X8', 'vueltas': 9.5, 'peso_por_resorte': 46.7},

    {'tipo': '12X7', 'vueltas': 5.5, 'peso_por_resorte': 32.7},
    {'tipo': '12X7', 'vueltas': 6, 'peso_por_resorte': 34.3},
    {'tipo': '12X7', 'vueltas': 6.5, 'peso_por_resorte': 36},
    {'tipo': '12X7', 'vueltas': 7, 'peso_por_resorte': 37.8},
    {'tipo': '12X7', 'vueltas': 7.5, 'peso_por_resorte': 39.7},
    {'tipo': '12X7', 'vueltas': 8, 'peso_por_resorte': 41.7},
    {'tipo': '12X7', 'vueltas': 8.5, 'peso_por_resorte': 43.8},
 
    {'tipo': '12X8', 'vueltas': 5.5, 'peso_por_resorte': 38},
    {'tipo': '12X8', 'vueltas': 6, 'peso_por_resorte': 39.9},
    {'tipo': '12X8', 'vueltas': 6.5, 'peso_por_resorte': 41.9},
    {'tipo': '12X8', 'vueltas': 7, 'peso_por_resorte': 43.9},
    {'tipo': '12X8', 'vueltas': 7.5, 'peso_por_resorte': 46.1},
    {'tipo': '12X8', 'vueltas': 8, 'peso_por_resorte': 48.4},
    {'tipo': '12X8', 'vueltas': 8.5, 'peso_por_resorte': 50.9},
    {'tipo': '12X8', 'vueltas': 9, 'peso_por_resorte': 53.4},
    {'tipo': '12X8', 'vueltas': 9.5, 'peso_por_resorte': 56.1},

    {'tipo': '14X7', 'vueltas': 5.5, 'peso_por_resorte': 38.1},
    {'tipo': '14X7', 'vueltas': 6, 'peso_por_resorte': 40},
    {'tipo': '14X7', 'vueltas': 6.5, 'peso_por_resorte': 42},
    {'tipo': '14X7', 'vueltas': 7, 'peso_por_resorte': 44.1},
    {'tipo': '14X7', 'vueltas': 7.5, 'peso_por_resorte': 46.3},
    {'tipo': '14X7', 'vueltas': 8, 'peso_por_resorte': 48.6},
    {'tipo': '14X7', 'vueltas': 8.5, 'peso_por_resorte': 51},
   
    {'tipo': '14X8', 'vueltas': 5.5, 'peso_por_resorte': 39.5},
    {'tipo': '14X8', 'vueltas': 6, 'peso_por_resorte': 41.5},
    {'tipo': '14X8', 'vueltas': 6.5, 'peso_por_resorte': 43.6},
    {'tipo': '14X8', 'vueltas': 7, 'peso_por_resorte': 45.8},
    {'tipo': '14X8', 'vueltas': 7.5, 'peso_por_resorte': 48.1},
    {'tipo': '14X8', 'vueltas': 8, 'peso_por_resorte': 50.5},
    {'tipo': '14X8', 'vueltas': 8.5, 'peso_por_resorte': 53},
    {'tipo': '14X8', 'vueltas': 9, 'peso_por_resorte': 55.7},
    {'tipo': '14X8', 'vueltas': 9.5, 'peso_por_resorte': 58.4},
   
    {'tipo': '16X7', 'vueltas': 5.5, 'peso_por_resorte': 43.5},
    {'tipo': '16X7', 'vueltas': 6, 'peso_por_resorte': 45.7},
    {'tipo': '16X7', 'vueltas': 6.5, 'peso_por_resorte': 48},
    {'tipo': '16X7', 'vueltas': 7, 'peso_por_resorte': 50.4},
    {'tipo': '16X7', 'vueltas': 7.5, 'peso_por_resorte': 52.9},
    {'tipo': '16X7', 'vueltas': 8, 'peso_por_resorte': 55.6},
    {'tipo': '16X7', 'vueltas': 8.5, 'peso_por_resorte': 58.3},
   
    {'tipo': '16X8', 'vueltas': 5.5, 'peso_por_resorte': 50.6},
    {'tipo': '16X8', 'vueltas': 6, 'peso_por_resorte': 53.1},
    {'tipo': '16X8', 'vueltas': 6.5, 'peso_por_resorte': 55.8},
    {'tipo': '16X8', 'vueltas': 7, 'peso_por_resorte': 58.6},
    {'tipo': '16X8', 'vueltas': 7.5, 'peso_por_resorte': 61.5},
    {'tipo': '16X8', 'vueltas': 8, 'peso_por_resorte': 64.6},
    {'tipo': '16X8', 'vueltas': 8.5, 'peso_por_resorte': 67.8},
    {'tipo': '16X8', 'vueltas': 9, 'peso_por_resorte': 71.2},
    {'tipo': '16X8', 'vueltas': 9.5, 'peso_por_resorte': 74.8},
 
    {'tipo': '18X7', 'vueltas': 5.5, 'peso_por_resorte': 48.9},
    {'tipo': '18X7', 'vueltas': 6, 'peso_por_resorte': 51.3},
    {'tipo': '18X7', 'vueltas': 6.5, 'peso_por_resorte': 53.9},
    {'tipo': '18X7', 'vueltas': 7, 'peso_por_resorte': 56.6},
    {'tipo': '18X7', 'vueltas': 7.5, 'peso_por_resorte': 59.4},
    {'tipo': '18X7', 'vueltas': 8, 'peso_por_resorte': 62.4},
    {'tipo': '18X7', 'vueltas': 8.5, 'peso_por_resorte': 65.5},

    {'tipo': '18X8', 'vueltas': 5.5, 'peso_por_resorte': 56.8},
    {'tipo': '18X8', 'vueltas': 6, 'peso_por_resorte': 59.7},
    {'tipo': '18X8', 'vueltas': 6.5, 'peso_por_resorte': 62.7},
    {'tipo': '18X8', 'vueltas': 7, 'peso_por_resorte': 65.8},
    {'tipo': '18X8', 'vueltas': 7.5, 'peso_por_resorte': 69.1},
    {'tipo': '18X8', 'vueltas': 8, 'peso_por_resorte': 72.5},
    {'tipo': '18X8', 'vueltas': 8.5, 'peso_por_resorte': 76.2},
    {'tipo': '18X8', 'vueltas': 9, 'peso_por_resorte': 80},
    {'tipo': '18X8', 'vueltas': 9.5, 'peso_por_resorte': 84},
   
    {'tipo': '20X7', 'vueltas': 5.5, 'peso_por_resorte': 53.6},
    {'tipo': '20X7', 'vueltas': 6, 'peso_por_resorte': 56.3},
    {'tipo': '20X7', 'vueltas': 6.5, 'peso_por_resorte': 59.1},
    {'tipo': '20X7', 'vueltas': 7, 'peso_por_resorte': 62.1},
    {'tipo': '20X7', 'vueltas': 7.5, 'peso_por_resorte': 65.2},
    {'tipo': '20X7', 'vueltas': 8, 'peso_por_resorte': 68.4},
    {'tipo': '20X7', 'vueltas': 8.5, 'peso_por_resorte': 71.8},
   
    {'tipo': '20X8', 'vueltas': 5.5, 'peso_por_resorte': 62.3},
    {'tipo': '20X8', 'vueltas': 6, 'peso_por_resorte': 65.4},
    {'tipo': '20X8', 'vueltas': 6.5, 'peso_por_resorte': 68.7},
    {'tipo': '20X8', 'vueltas': 7, 'peso_por_resorte': 72.2},
    {'tipo': '20X8', 'vueltas': 7.5, 'peso_por_resorte': 75.8},
    {'tipo': '20X8', 'vueltas': 8, 'peso_por_resorte': 79.6},
    {'tipo': '20X8', 'vueltas': 8.5, 'peso_por_resorte': 83.5},
    {'tipo': '20X8', 'vueltas': 9, 'peso_por_resorte': 87.7},
    {'tipo': '20X8', 'vueltas': 9.5, 'peso_por_resorte': 92.1},

    {'tipo': '24X7', 'vueltas': 5.5, 'peso_por_resorte': 65.3},
    {'tipo': '24X7', 'vueltas': 6, 'peso_por_resorte': 68.6},
    {'tipo': '24X7', 'vueltas': 6.5, 'peso_por_resorte': 72},
    {'tipo': '24X7', 'vueltas': 7, 'peso_por_resorte': 75.6},
    {'tipo': '24X7', 'vueltas': 7.5, 'peso_por_resorte': 79.4},
    {'tipo': '24X7', 'vueltas': 8, 'peso_por_resorte': 83.3},
    {'tipo': '24X7', 'vueltas': 8.5, 'peso_por_resorte': 87.5},
   
    {'tipo': '24X8', 'vueltas': 5.5, 'peso_por_resorte': 75.9},
    {'tipo': '24X8', 'vueltas': 6, 'peso_por_resorte': 79.7},
    {'tipo': '24X8', 'vueltas': 6.5, 'peso_por_resorte': 83.7},
    {'tipo': '24X8', 'vueltas': 7, 'peso_por_resorte': 87.9},
    {'tipo': '24X8', 'vueltas': 7.5, 'peso_por_resorte': 92.3},
    {'tipo': '24X8', 'vueltas': 8, 'peso_por_resorte': 96.9},
    {'tipo': '24X8', 'vueltas': 8.5, 'peso_por_resorte': 101.7},
    {'tipo': '24X8', 'vueltas': 9, 'peso_por_resorte': 106.8},
    {'tipo': '24X8', 'vueltas': 9.5, 'peso_por_resorte': 112.2},
   
]

def calcular_vueltas(altura):
    PIE = 30.5  # cm
    return altura / PIE

def encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes, intercalar=True):
    combinaciones_validas = []
    
    if intercalar:
        # Generar combinaciones intercaladas
        for combo in itertools.product(resortes, repeat=num_resortes):
            if all(abs(resorte['vueltas'] - vueltas) <= 0.5 for resorte in combo):
                peso_combinado = sum(resorte['peso_por_resorte'] for resorte in combo)
                if abs(peso_combinado - peso_objetivo) <= 4:
                    combinaciones_validas.append(combo)
    else:
        # Generar combinaciones sin intercalar
        for resorte in resortes:
            if abs(resorte['vueltas'] - vueltas) <= 0.5:
                for combo in itertools.combinations([resorte] * num_resortes, num_resortes):
                    peso_combinado = sum(r['peso_por_resorte'] for r in combo)
                    if abs(peso_combinado - peso_objetivo) <= 4:
                        combinaciones_validas.append(combo)

    # Ordenar las combinaciones válidas según su cercanía al peso objetivo
    combinaciones_validas.sort(key=lambda combo: abs(sum(resorte['peso_por_resorte'] for resorte in combo) - peso_objetivo))
    
    return combinaciones_validas

@resortes_blueprint.route('/', methods=['GET', 'POST'])
def index():
    tipos_unicos = {resorte['tipo'] for resorte in resortes}
    if request.method == 'POST':
        peso_objetivo = float(request.form['peso'])
        altura = float(request.form['altura']) * 100
        vueltas = calcular_vueltas(altura)

        combinaciones_por_numero = {}
        max_num_resortes = 3

        for num_resortes in range(1, max_num_resortes + 1):
            combinaciones = encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes)
            if combinaciones:
                combinaciones_por_numero[num_resortes] = combinaciones

        return render_template('resultados.html', 
                               combinaciones_por_numero=combinaciones_por_numero,
                               tipos_unicos=tipos_unicos,
                               tipos_seleccionados=tipos_unicos,
                               peso=peso_objetivo,
                               altura=altura / 100)
    else:
        return render_template('resortes.html', tipos_unicos=tipos_unicos)

@resortes_blueprint.route('/filtrar_resultados', methods=['POST'])
def filtrar_resultados():
    peso_objetivo = float(request.form['peso'])
    altura = float(request.form['altura']) * 100
    vueltas = calcular_vueltas(altura)
    tipos_seleccionados = request.form.getlist('resortes_disponibles')

    resortes_filtrados = [resorte for resorte in resortes if resorte['tipo'] in tipos_seleccionados]

    max_num_resortes = 3
    combinaciones_por_numero = {}
    for num_resortes in range(1, max_num_resortes + 1):
        combinaciones = encontrar_combinaciones(peso_objetivo, vueltas, resortes_filtrados, num_resortes)
        if combinaciones:
            combinaciones_por_numero[num_resortes] = combinaciones

    tipos_unicos = {resorte['tipo'] for resorte in resortes}
    return render_template('resultados.html',
                           combinaciones_por_numero=combinaciones_por_numero,
                           tipos_unicos=tipos_unicos,
                           tipos_seleccionados=tipos_seleccionados,
                           peso=peso_objetivo,
                           altura=altura / 100)

@resortes_blueprint.route('/imprimir_ticket')
def imprimir_ticket():
    peso = request.args.get('peso')
    altura = request.args.get('altura')
    resortes_query = request.args.getlist('resortes')

    resortes_seleccionados = [res.split('-') for res in resortes_query]
    resortes = [{'tipo': tipo.strip(), 'vueltas': vueltas.strip(), 'peso': peso_resorte.strip()} for tipo, vueltas, peso_resorte in resortes_seleccionados]

    return render_template('ticket.html', peso=peso, altura=altura, resortes=resortes)





