IVA = 15

def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_iva(subtotal):
    return subtotal * IVA / 100


def calcular_total(subtotal, impuesto):
    return subtotal + impuesto
