import os


def main():
    mensaje = "Bienvenido a Tienda Vale Todo"
    nombre = None
    descripcion1 = descripcion2 = ""
    precio1 = precio2 = 0.0
    cantidad1 = cantidad2 = 0
    porcentaje = 0.0
    impuesto = 0.15
    tasa_recargo = 0.10
    condicion = ""
    subtotal = descuento = iva = recargo = total = 0.0

    nombre = leer_cliente(mensaje)

    #Cambio #1
    descripcion1 = input("Ingrese el nombre del producto 1: ")
    precio1 = float(input("Ingrese el precio del producto 1: "))
    cantidad1 = int(input("Ingrese la cantidad del producto 1: "))

    descripcion2 = input("Ingrese el nombre del producto 2: ")
    precio2 = float(input("Ingrese el precio del producto 2: "))
    cantidad2 = int(input("Ingrese la cantidad del producto 2: "))

    porcentaje = float(input("Ingrese el porcentaje de descuento: "))

    #Cambio #2
    condicion = input("Condición de venta (contado/credito): ").strip().lower()

    subtotal, descuento, iva, recargo, total = calcular_total(
        precio1, cantidad1, precio2, cantidad2,
        porcentaje, impuesto, condicion, tasa_recargo
    )
    mostrar_factura(nombre, descripcion1, precio1, cantidad1,
                    descripcion2, precio2, cantidad2,
                    porcentaje, impuesto, condicion,
                    subtotal, descuento, iva, recargo, total)


def leer_cliente(mensaje):
    os.system("cls")
    print(mensaje)
    print("*" * 30)
    nombre = input("Ingrese el nombre del cliente: ")
    return nombre


def calcular_total(precio1, cantidad1, precio2, cantidad2,
                   porcentaje, impuesto, condicion, tasa_recargo):
    subtotal = calcular_total_productos(precio1, cantidad1, precio2, cantidad2)
    descuento = calcular_descuento(subtotal, porcentaje)
    iva = subtotal * impuesto
    total = subtotal + iva - descuento
    recargo = calcular_recargo(total, condicion, tasa_recargo)
    total = total + recargo
    return subtotal, descuento, iva, recargo, total


#Cambio #1
def calcular_total_productos(precio1, cantidad1, precio2, cantidad2):
    subtotal1 = calcular_subtotal(precio1, cantidad1)
    subtotal2 = calcular_subtotal(precio2, cantidad2)
    return subtotal1 + subtotal2


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje / 100
    return descuento


#Cambio #2
def calcular_recargo(total, condicion, tasa_recargo):
    recargo = 0.0
    if condicion == "credito" or condicion == "crédito":
        recargo = total * tasa_recargo
    return recargo


def mostrar_factura(nombre, descripcion1, precio1, cantidad1,
                    descripcion2, precio2, cantidad2,
                    porcentaje, impuesto, condicion,
                    subtotal, descuento, iva, recargo, total):
    os.system("cls")
    print("*" * 50)
    print("Factura de Compra".center(50))
    print("*" * 50)
    print(f"Cliente: {nombre}")
    print(f"Condición de venta: {condicion}")
    print("-" * 50)
    print(f"{'Producto':<20}{'Precio':>10}{'Cant.':>8}{'Importe':>12}")
    print(f"{descripcion1:<20}{precio1:>10.2f}{cantidad1:>8}{precio1 * cantidad1:>12.2f}")
    print(f"{descripcion2:<20}{precio2:>10.2f}{cantidad2:>8}{precio2 * cantidad2:>12.2f}")
    print("-" * 50)
    print(f"{'Subtotal:':<30}{subtotal:>20.2f}")
    print(f"{f'Descuento ({porcentaje:.0f}%):':<30}{descuento:>20.2f}")
    print(f"{f'IVA ({impuesto * 100:.0f}%):':<30}{iva:>20.2f}")
    print(f"{'Recargo:':<30}{recargo:>20.2f}")
    print(f"{'TOTAL:':<30}{total:>20.2f}")
    print("*" * 50)


main()