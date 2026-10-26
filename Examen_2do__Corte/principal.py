from pila import *
import os

def main():
    pila = Stack()
    opcion = 0
    while True:
        os.system("cls")
        print("--------------------------------")
        print("---GESTION DE PRODUCTOS (PILA)--")
        print("--------------------------------")
        print("1. Agregar Producto")
        print("2. Sacar Producto")
        print("3. Ver Tope")
        print("4. Buscar Producto")
        print("5. Mostrar Pila")
        print("6. Vaciar Pila")
        print("7. Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            opcion = 0
        match opcion:
            case 1:
                try:
                    id = int(input("Ingrese el ID del producto: "))
                    nombre = input("Ingrese el nombre del producto: ")
                    precio = float(input("Ingrese el precio del producto: "))
                    stock = int(input("Ingrese el stock del producto: "))
                    if pila.search(id) != None:
                        print("Ya existe un producto con ese ID")
                    else:
                        pila.push(Product(id, nombre, precio, stock))
                        print("Producto agregado")
                except ValueError:
                    print("Dato invalido")
            case 2:
                prod = pila.pop()
                if prod != None:
                    print("Producto sacado:")
                    prod.print()
                else:
                    print("La pila esta vacia")
            case 3:
                prod = pila.peek()
                if prod != None:
                    print("Producto en el tope:")
                    prod.print()
                else:
                    print("La pila esta vacia")
            case 4:
                try:
                    id = int(input("Ingrese el ID del producto a buscar: "))
                    prod = pila.search(id)
                    if prod != None:
                        print("Producto encontrado:")
                        prod.print()
                    else:
                        print("Producto no encontrado")
                except ValueError:
                    print("Dato invalido")
            case 5:
                if pila.isEmpty():
                    print("La pila esta vacia")
                else:
                    pila.print()
            case 6:
                productos = pila.clear()
                print(f"Se sacaron {len(productos)} productos:")
                for p in productos:
                    p.print()
            case 7:
                break
            case _:
                print("Opcion no valida")
        input("Presione Enter para continuar...")

main()