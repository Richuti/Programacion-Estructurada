import os
def main():
    mensaje = "Bienvenido a Tienda Vale Todo",
    nombre = none,
    precio = 0.0,
    cantidad = 0,
    porcentaje = 0.0,
    impuesto = 0.15,
    total = subtotal = descuento = 0.0,

    nombre = leer_nombre(mensaje)

    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    porcentaje = float(input("Ingrese el porcentaje de descuento: "))
    total, subtotal, descuento = calcular_total(precio, cantidad, porcentaje, impuesto)
    mostrar_factura(nombre, precio, cantidad, porcentaje, impuesto, total, subtotal, descuento)

def leer_nombre(mensaje):
    os.system("cls")
    print(mensaje)
    print("*"*20)
    nombre = input("Ingrese el nombre del cliente: ")
    return nombre

def calcular_total(precio, cantidad, porcentaje, impuesto):
    subtotal = calcular_subtotal(precio, cantidad)
    desceunto = calcular_descuento(subtotal, porcentaje)
    iva = subtotal * impuesto
    total = subtotal + iva - descuento
    return total

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje / 100
    return descuento

def mostrar_factura(nombre, precio, cantidad, porcentaje, impuesto, total, subtotal, descuento):
    os.system("cls")
    print("*"*20)
    print("Factura de Compra")
    print("*"*20)
    print(f"Nombre del cliente: {nombre}")
    print(f"Precio del producto: {precio}")
    print(f"Cantidad del producto: {cantidad}")
    print(f"Porcentaje de descuento: {porcentaje}")
    print(f"Impuesto: {impuesto}")
    print(f"Total: {total}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")

