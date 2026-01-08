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
   
    # {'tipo': '14X8', 'vueltas': 5.5, 'peso_por_resorte': 39.5},
    # {'tipo': '14X8', 'vueltas': 6, 'peso_por_resorte': 41.5},
    # {'tipo': '14X8', 'vueltas': 6.5, 'peso_por_resorte': 43.6},
    # {'tipo': '14X8', 'vueltas': 7, 'peso_por_resorte': 45.8},
    # {'tipo': '14X8', 'vueltas': 7.5, 'peso_por_resorte': 48.1},
    # {'tipo': '14X8', 'vueltas': 8, 'peso_por_resorte': 50.5},
    # {'tipo': '14X8', 'vueltas': 8.5, 'peso_por_resorte': 53},
    # {'tipo': '14X8', 'vueltas': 9, 'peso_por_resorte': 55.7},
    # {'tipo': '14X8', 'vueltas': 9.5, 'peso_por_resorte': 58.4},

    {'tipo': '14X8', 'vueltas': 5.5, 'peso_por_resorte': 44.3},
    {'tipo': '14X8', 'vueltas': 6, 'peso_por_resorte': 46.5},
    {'tipo': '14X8', 'vueltas': 6.5, 'peso_por_resorte': 48.8},
    {'tipo': '14X8', 'vueltas': 7, 'peso_por_resorte': 51.3},
    {'tipo': '14X8', 'vueltas': 7.5, 'peso_por_resorte': 53.8},
    {'tipo': '14X8', 'vueltas': 8, 'peso_por_resorte': 56.5},
    {'tipo': '14X8', 'vueltas': 8.5, 'peso_por_resorte': 59.3},
    {'tipo': '14X8', 'vueltas': 9, 'peso_por_resorte': 62.3},
    {'tipo': '14X8', 'vueltas': 9.5, 'peso_por_resorte': 65.4},
   
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
   
    {'tipo': '28X7', 'vueltas': 5.5, 'peso_por_resorte': 76.2},
    {'tipo': '28X7', 'vueltas': 6, 'peso_por_resorte': 80.0},
    {'tipo': '28X7', 'vueltas': 6.5, 'peso_por_resorte': 84.0},
    {'tipo': '28X7', 'vueltas': 7, 'peso_por_resorte': 88.2},
    {'tipo': '28X7', 'vueltas': 7.5, 'peso_por_resorte': 92.6},
    {'tipo': '28X7', 'vueltas': 8, 'peso_por_resorte': 97.2},
    {'tipo': '28X7', 'vueltas': 8.5, 'peso_por_resorte': 102.1},

    {'tipo': '28X8', 'vueltas': 5.5, 'peso_por_resorte': 88.6},
    {'tipo': '28X8', 'vueltas': 6, 'peso_por_resorte': 93.0},
    {'tipo': '28X8', 'vueltas': 6.5, 'peso_por_resorte': 97.7},
    {'tipo': '28X8', 'vueltas': 7, 'peso_por_resorte': 102.5},
    {'tipo': '28X8', 'vueltas': 7.5, 'peso_por_resorte': 107.7},
    {'tipo': '28X8', 'vueltas': 8, 'peso_por_resorte': 113.0},
    {'tipo': '28X8', 'vueltas': 8.5, 'peso_por_resorte': 118.7},
    {'tipo': '28X8', 'vueltas': 9, 'peso_por_resorte': 124.6},
    {'tipo': '28X8', 'vueltas': 9.5, 'peso_por_resorte': 130.9},

]

# CÁLCULO DE VUELTAS
# ======================================================
# def calcular_vueltas(altura_cm):
#     PIE = 30.5
#     return altura_cm / PIE

def calcular_vueltas(altura_cm):
    """
    Calcula las vueltas reales del portón considerando
    el cambio de sistema arriba de 3.00 m
    """

    if altura_cm <= 300:
        vueltas_reales = altura_cm / 30.5
    else:
        vueltas_reales = altura_cm / 43

    # Precarga obligatoria
    vueltas_reales += 0.5

    # Normalización mecánica:
    # 0.00 – 0.24 → .0
    # 0.25 – 0.74 → .5
    # 0.75 – 0.99 → siguiente entero
    entero = int(vueltas_reales)
    decimal = vueltas_reales - entero

    if decimal < 0.25:
        vueltas_finales = float(entero)
    elif decimal < 0.75:
        vueltas_finales = entero + 0.5
    else:
        vueltas_finales = float(entero + 1)

    return round(vueltas_finales, 2)



def normalizar_vueltas(vueltas):
    """
    Regla mecánica correcta:
    0.00–0.24 → baja
    0.25–0.74 → .5
    0.75–0.99 → sube
    """
    base = int(vueltas)
    dec = vueltas - base

    if dec < 0.25:
        return float(base)
    elif dec < 0.75:
        return base + 0.5
    else:
        return float(base + 1)

# ============SELECCIÓN AUTOMÁTICA FINAL=======================
def seleccionar_resorte_automatico(peso_objetivo, vueltas_reales, resortes):
    """
    Flujo correcto:
    1) Vueltas reales + 0.5 precarga
    2) Normalizar vueltas
    3) Buscar SOLO en esa vuelta
    4) Jerarquía:
       - 2 resortes iguales
       - 1 resorte
       - 3 resortes
    """

    # vueltas_objetivo = normalizar_vueltas(vueltas_reales + 0.5)
    vueltas_objetivo = normalizar_vueltas(vueltas_reales)

    tolerancia = 4

    resortes_vuelta = [
        r for r in resortes
        if r['vueltas'] == vueltas_objetivo
    ]

    if not resortes_vuelta:
        return None

    # ==============DOS RESORTES IGUALES====================
    candidatos = []
    for r in resortes_vuelta:
        peso_total = r['peso_por_resorte'] * 2
        if abs(peso_total - peso_objetivo) <= tolerancia:
            candidatos.append((abs(peso_total - peso_objetivo), [r, r]))

    if candidatos:
        return min(candidatos, key=lambda x: x[0])[1]

    # ==============UN SOLO RESORTE=====================
    for r in resortes_vuelta:
        if abs(r['peso_por_resorte'] - peso_objetivo) <= tolerancia:
            return [r]

    # ===================TRES RESORTES==================
    for combo in itertools.combinations_with_replacement(resortes_vuelta, 3):
        peso_total = sum(r['peso_por_resorte'] for r in combo)
        if abs(peso_total - peso_objetivo) <= tolerancia:
            return list(combo)

    return None

# ================RUTA PRINCIPAL========================
@resortes_blueprint.route('/', methods=['GET', 'POST'])
def index():
    tipos_unicos = {r['tipo'] for r in resortes}

    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura_m = float(request.form['altura'])
        altura_cm = altura_m * 100

        vueltas_reales = calcular_vueltas(altura_cm)

        seleccion = seleccionar_resorte_automatico(
            peso,
            vueltas_reales,
            resortes
        )

        return render_template(
            'resultados.html',
            seleccion=seleccion,
            peso=peso,
            altura=altura_m,
            vueltas=round(vueltas_reales, 2)
        )

    return render_template('resortes.html', tipos_unicos=tipos_unicos)




