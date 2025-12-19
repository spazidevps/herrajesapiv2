def calcular_rieles(cantidad_paneles_46cm, cantidad_paneles_53cm):
    # Alturas de los paneles
    altura_panel_46cm = 0.46  # en metros
    altura_panel_53cm = 0.53  # en metros

    # Calcula la altura total
    altura_total = (cantidad_paneles_46cm * altura_panel_46cm) + (cantidad_paneles_53cm * altura_panel_53cm)

    # Determina el juego de rieles  necesario
    if altura_total <= 2.24:
        return "Entregar juego de rieles de 2.14m"
    elif altura_total <= 2.56:
        return "Entregar juego de rieles de 2.44m"
    elif altura_total <= 3.08:
        return "Entregar juego de rieles de 3m o vender un juego adicional"
    else:
        return "La altura total excede el límite máximo para los rieles disponibles"  