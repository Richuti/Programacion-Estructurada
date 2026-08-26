import os
from importlib import import_module

inventarioPulperia = import_module("if.inventarioPulperia").inventarioPulperia
promocionTienda = import_module("if.tienda").promocionTienda
metaVentas = import_module("if.meta").metaVentas
entregaComedor = import_module("if.comedor").entregaComedor
pesoProductos = import_module("if.productos").pesoProductos
creditoPulperia = import_module("if_anidados.pulperia").creditoPulperia
tarifaEntregas = import_module("if_anidados.entregas").tarifaEntregas
calidadCooperativa = import_module("if_anidados.cooperativa").calidadCooperativa
descuentoHospedaje = import_module("if_anidados.hospedaje").descuentoHospedaje
totalFerreteria = import_module("if_anidados.ferreteria").totalFerreteria


CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def mostrar_menu():
    print()
    print(f"{CYAN}{BOLD}  🛒  MENÚ DE EJERCICIOS  🛒{RESET}")
    print()
    print(f"  {YELLOW} 1{RESET}  📦  Inventario de pulpería")
    print(f"  {YELLOW} 2{RESET}  🏷️   Promoción de una tienda")
    print(f"  {YELLOW} 3{RESET}  🎯  Meta de ventas")
    print(f"  {YELLOW} 4{RESET}  🍽️   Entrega de un comedor")
    print(f"  {YELLOW} 5{RESET}  ⚖️   Peso de productos")
    print(f"  {YELLOW} 6{RESET}  🏪  Crédito pulpería")
    print(f"  {YELLOW} 7{RESET}  🚚  Entregas")
    print(f"  {YELLOW} 8{RESET}  ☕  Cooperativa")
    print(f"  {YELLOW} 9{RESET}  🏨  Hospedaje")
    print(f"  {YELLOW}10{RESET}  🔧  Ferretería")
    print(f"  {YELLOW}11{RESET}  🚪  Salir")
    print()


def main():
    while True:
        os.system("cls")
        mostrar_menu()

        opc = int(input(f"  {GREEN}👉 Seleccione una opción:{RESET} "))
        match opc:
            case 1:
                inventarioPulperia()
            case 2:
                promocionTienda()
            case 3:
                metaVentas()
            case 4:
                entregaComedor()
            case 5:
                pesoProductos()
            case 6:
                creditoPulperia()
            case 7:
                tarifaEntregas()
            case 8:
                calidadCooperativa()
            case 9:
                descuentoHospedaje()
            case 10:
                totalFerreteria()
            case 11:
                print(f"\n  {GREEN}👋 ¡Hasta luego!{RESET}")
                break
            case _:
                print(f"\n  {RED}❌ Opción no válida{RESET}")

        input(f"\n  {YELLOW}⏎  Presione Enter para continuar...{RESET}")


if __name__ == "__main__":
    main()
