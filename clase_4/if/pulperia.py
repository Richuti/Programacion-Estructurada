nombre_producto = input("Ingrese el nombre del producto: ")
cantidad_producto = int(input("Ingrese la cantidad del producto: "))

if cantidad_producto < 5:
    print(f"El producto {nombre_producto} tiene una cantidad menor a 5")
else:
    print(f"El producto {nombre_producto} tiene una gran cantidad")