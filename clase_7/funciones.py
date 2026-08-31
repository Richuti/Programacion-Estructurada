def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal, porcentaje):
    return subtotal - (subtotal * porcentaje / 100)

precio = float(input("Precio unitario C$: "))
cantidad = int(input("Cantidad: "))
subtotal = calcular_subtotal(precio, cantidad)
porcentaje = float(input("Introduzca su descuento: "))
total = aplicar_descuento(subtotal, porcentaje)
print("Subtotal C$: ", subtotal)
print("Descuento C$: ", aplicar_descuento(subtotal, porcentaje))
print("Total C$: ", total)