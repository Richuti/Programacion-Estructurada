import os

def menuPulperia():
    os.system("cls")

    productos = (
        ("Arroz", 25.0),
        ("Frijoles", 30.0),
        ("Azucar", 20.0),
        ("Aceite", 60.0),
        ("Cafe", 45.0),
    )

    print("*" * 30)
    print("   MENU DE LA PULPERIA")
    print("*" * 30)
    for i in range(len(productos)):
        nombre, precio = productos[i]
        print(f"{i + 1}. {nombre} - C${precio}")
    print("*" * 30)

    opcion = int(input("Seleccione el numero del producto: "))

    if opcion >= 1 and opcion <= len(productos):
        nombre, precio = productos[opcion - 1]
        cantidad = int(input(f"Cantidad de {nombre}: "))
        total = precio * cantidad
        print(f"Total a pagar por {cantidad} de {nombre}: C${total}")
    else:
        print("Producto no valido")

    print(f"La pulperia tiene {len(productos)} productos en el menu")

if __name__ == "__main__":
    menuPulperia()
