nombre = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

total = precio * cantidad

print(f"Has comprado {cantidad} {nombre} a un precio de {precio} cada uno, el total es de {total}")