import os
os.system("cls")

reposiciones = 0

for producto in range(1, 9):
    cantidad = int(input(f"Ingrese la cantidad del producto {producto}: "))
    if cantidad < 10:
        print(f"El producto {producto} tiene inventario bajo")
        reposiciones = reposiciones + 1

print(f"Se necesitan {reposiciones} reposiciones")
