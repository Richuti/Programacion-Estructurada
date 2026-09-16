import os


def main():
    mensaje = "Bienvenido a Tienda Vale Todo"
    nombre = None
    productos = []
    porcentaje = 0.0
    impuesto = 0.15
    tasa_recargo = 0.10         
    condicion = ""
    subtotal = descuento = iva = recargo = total = 0.0

    nombre = leer_cliente(mensaje)

    #Cambio #1
    continuar = "s"
    while continuar.strip().lower() == "s":
        descripcion = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        productos.append({"descripcion": descripcion, "precio": precio, "cantidad": cantidad})
        continuar = input("¿Desea agregar otro producto? (s/n): ")

    porcentaje = float(input("Ingrese el porcentaje de descuento: "))

    #Cambio #2
    condicion = input("Condición de venta (contado/credito): ").strip().lower()

    subtotal, descuento, iva, recargo, total = calcular_total(
        productos, porcentaje, impuesto, condicion, tasa_recargo
    )
    mostrar_factura(nombre, productos, porcentaje, impuesto, condicion,
                    subtotal, descuento, iva, recargo, total)


def leer_cliente(mensaje):
    os.system("cls")
    print(mensaje)
    print("*" * 30)
    nombre = input("Ingrese el nombre del cliente: ")
    return nombre


def calcular_total(productos, porcentaje, impuesto, condicion, tasa_recargo):
    subtotal = calcular_total_productos(productos)
    descuento = calcular_descuento(subtotal, porcentaje)
    iva = subtotal * impuesto
    total = subtotal + iva - descuento
    recargo = calcular_recargo(total, condicion, tasa_recargo)
    total = total + recargo
    return subtotal, descuento, iva, recargo, total


#Cambio #1
def calcular_total_productos(productos):
    acumulado = 0.0
    for producto in productos:
        acumulado += calcular_subtotal(producto["precio"], producto["cantidad"])
    return acumulado


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje / 100
    return descuento


#Cambio #2
def calcular_recargo(total, condicion, tasa_recargo):
    recargo = 0.0
    if condicion in ("credito", "crédito"):
        recargo = total * tasa_recargo
    return recargo


def mostrar_factura(nombre, productos, porcentaje, impuesto, condicion,
                    subtotal, descuento, iva, recargo, total):
    os.system("cls")
    print("*" * 50)
    print("Factura de Compra".center(50))
    print("*" * 50)
    print(f"Cliente: {nombre}")
    print(f"Condición de venta: {condicion}")
    print("-" * 50)
    print(f"{'Producto':<20}{'Precio':>10}{'Cant.':>8}{'Importe':>12}")
    for p in productos:
        importe = p["precio"] * p["cantidad"]
        print(f"{p['descripcion']:<20}{p['precio']:>10.2f}{p['cantidad']:>8}{importe:>12.2f}")
    print("-" * 50)
    print(f"{'Subtotal:':<30}{subtotal:>20.2f}")
    print(f"{f'Descuento ({porcentaje:.0f}%):':<30}{descuento:>20.2f}")
    print(f"{f'IVA ({impuesto * 100:.0f}%):':<30}{iva:>20.2f}")
    print(f"{'Recargo:':<30}{recargo:>20.2f}")
    print(f"{'TOTAL:':<30}{total:>20.2f}")
    print("*" * 50)

main()


