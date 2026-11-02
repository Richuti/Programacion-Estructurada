import os
IVA = 15

def leer_numero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            numero = float(texto)
        except ValueError:
            print("Error: debe ingresar un numero")
        else:
            if numero < 0:
                print("Error: el numero no puede ser negativo")
            else:
                return numero


def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_total(subtotal, descuento, impuesto):
    return subtotal - descuento + impuesto


def mostrar_factura(subtotal, descuento, impuesto, total):
    print()
    print("--------- FACTURA ---------")
    print(f"Subtotal:   C$ {round(subtotal, 2)}")
    print(f"Descuento:  C$ {round(descuento, 2)}")
    print(f"IVA {IVA}%:    C$ {round(impuesto, 2)}")
    print(f"Total:      C$ {round(total, 2)}")
    print("---------------------------")


precio = leer_numero("Ingrese el precio unitario: ")
cantidad = leer_numero("Ingrese la cantidad: ")
porcentaje = leer_numero("Ingrese el descuento (%): ")

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje)
impuesto = calcular_descuento(subtotal - descuento, IVA)
total = calcular_total(subtotal, descuento, impuesto)

os.system("cls")
mostrar_factura(subtotal, descuento, impuesto, total)
