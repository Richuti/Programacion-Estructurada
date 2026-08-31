import os

from facturacion.lectura import leer_texto, leer_numero, leer_entero
from facturacion.calculos import calcular_subtotal, calcular_iva, calcular_total
from facturacion.presentacion import mostrar_factura, mostrar_error

def facturacion_modular():
    os.system("cls")
    print("RETO 8: Facturacion modular")
    print("Integra lectura segura, calculos y presentacion en modulos propios.")
    print()

    print("Prueba 1 -> subtotal de 25.50 x 4:", calcular_subtotal(25.50, 4))
    print("Prueba 2 -> iva de 102:", calcular_iva(102))
    print("Prueba 3 -> total de 102 + 15.3:", calcular_total(102, 15.3))
    print()

    producto = leer_texto("Ingrese el producto: ")
    precio = leer_numero("Ingrese el precio unitario: ")
    cantidad = leer_entero("Ingrese la cantidad: ")

    if precio is None or cantidad is None:
        mostrar_error("el precio y la cantidad deben ser numeros positivos")
        return

    subtotal = calcular_subtotal(precio, cantidad)
    impuesto = calcular_iva(subtotal)
    total = calcular_total(subtotal, impuesto)

    mostrar_factura(producto, cantidad, subtotal, impuesto, total)

if __name__ == "__main__":
    facturacion_modular()
