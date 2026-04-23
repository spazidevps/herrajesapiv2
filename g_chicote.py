def asignar_chicote(altura):
    """
    Calcula el chicote como:
    altura + 0.40 m

    Retorna un float redondeado a 2 decimales.
    """

    if altura is None or altura <= 0:
        return "Altura no válida"

    chicote = altura + 0.40

    # return round(chicote, 2)
    return float(f"{chicote:.2f}")
