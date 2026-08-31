import os

from excepciones.precio import precioProducto
from excepciones.cantidad import cantidadProductos
from excepciones.calificacion import calificacionEstudiante
from excepciones.edad import edadRegistro
from excepciones.registro import registroEmpleado
from operaciones.promedio import promedioVentas
from operaciones.descuento import descuentoProporcional
from operaciones.moneda import conversionMoneda
from operaciones.tipos import tiposIncompatibles
from operaciones.comision import calculoComision
from estructuras.inventario import indiceInventario
from estructuras.empleados import diccionarioEmpleados
from estructuras.menu import menuOpciones
from recursos.archivo import archivoReportes
from recursos.importacion import importacionControlada


CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def mostrar_menu():
    print()
    print(f"{CYAN}{BOLD}  ⚠️   MENÚ DE EXCEPCIONES  ⚠️{RESET}")
    print()
    print(f"  {CYAN}ENTRADAS{RESET}")
    print(f"  {YELLOW} 1{RESET}  🏷️   Precio de un producto")
    print(f"  {YELLOW} 2{RESET}  🧮  Cantidad de productos")
    print(f"  {YELLOW} 3{RESET}  📊  Calificación")
    print(f"  {YELLOW} 4{RESET}  🎂  Edad para registro")
    print(f"  {YELLOW} 5{RESET}  📝  Tres entradas consecutivas")
    print()
    print(f"  {CYAN}OPERACIONES{RESET}")
    print(f"  {YELLOW} 6{RESET}  📈  Promedio de ventas")
    print(f"  {YELLOW} 7{RESET}  🏷️   Descuento proporcional")
    print(f"  {YELLOW} 8{RESET}  💱  Conversión de moneda")
    print(f"  {YELLOW} 9{RESET}  ⚡  Tipos incompatibles")
    print(f"  {YELLOW}10{RESET}  💵  Cálculo de comisión")
    print()
    print(f"  {CYAN}ESTRUCTURAS{RESET}")
    print(f"  {YELLOW}11{RESET}  📦  Índice de inventario")
    print(f"  {YELLOW}12{RESET}  👥  Diccionario de empleados")
    print(f"  {YELLOW}13{RESET}  📋  Menú de opciones")
    print()
    print(f"  {CYAN}RECURSOS{RESET}")
    print(f"  {YELLOW}14{RESET}  📄  Archivo de reportes")
    print(f"  {YELLOW}15{RESET}  📥  Importación controlada")
    print()
    print(f"  {YELLOW}16{RESET}  🚪  Salir")
    print()


def main():
    while True:
        os.system("cls")
        mostrar_menu()

        opc = int(input(f"  {GREEN}👉 Seleccione una opción:{RESET} "))
        match opc:
            case 1:
                precioProducto()
            case 2:
                cantidadProductos()
            case 3:
                calificacionEstudiante()
            case 4:
                edadRegistro()
            case 5:
                registroEmpleado()
            case 6:
                promedioVentas()
            case 7:
                descuentoProporcional()
            case 8:
                conversionMoneda()
            case 9:
                tiposIncompatibles()
            case 10:
                calculoComision()
            case 11:
                indiceInventario()
            case 12:
                diccionarioEmpleados()
            case 13:
                menuOpciones()
            case 14:
                archivoReportes()
            case 15:
                importacionControlada()
            case 16:
                print(f"\n  {GREEN}👋 ¡Hasta luego!{RESET}")
                break
            case _:
                print(f"\n  {RED}❌ Opción no válida{RESET}")

        input(f"\n  {YELLOW}⏎  Presione Enter para continuar...{RESET}")


if __name__ == "__main__":
    main()
