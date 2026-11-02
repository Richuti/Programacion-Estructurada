def leer_texto(mensaje):
    return input(mensaje)


def leer_numero(mensaje):
    texto = input(mensaje)

    try:
        numero = float(texto)
    except ValueError:
        return None
    else:
        if numero < 0:
            return None
        return numero


def leer_entero(mensaje):
    texto = input(mensaje)

    try:
        numero = int(texto)
    except ValueError:
        return None
    else:
        if numero < 0:
            return None
        return numero
