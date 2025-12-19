def asignar_chicote(altura):
    if 1.59 <= altura <= 2.16:
        return 2.7
    elif 2.17 <= altura <= 2.65:
        return 3.0
    elif 2.66 <= altura <= 3.0:
        return 3.4
    elif 3.1 <= altura <= 3.31:
        return 3.8
    elif 3.39 <= altura <= 3.62:
        return 4.2
    elif 3.8 <= altura <= 4.0:
        return 4.6
    elif 4.9 <= altura <= 5.32:  # Corregido  basado en la suposición de un error tipográfico
        return 4.8
    else:
        return "No disponible para la altura ingresada"  
    
        