import os
from importlib import import_module

pesoCafe = import_module("for.cafe").pesoCafe
inventarioDistribuidora = import_module("for.distribuidora").inventarioDistribuidora
ventasMinisuper = import_module("for.minisuper").ventasMinisuper
produccionPanaderia = import_module("for.panaderia").produccionPanaderia
valoracionRestaurante = import_module("for.restaurante").valoracionRestaurante
controlAcceso = import_module("while.acceso").controlAcceso
cierreCaja = import_module("while.cierre_caja").cierreCaja
combustibleMotocicleta = import_module("while.motocicleta").combustibleMotocicleta
validarPedido = import_module("while.pedido").validarPedido
reposicionInventario = import_module("while.reposicion").reposicionInventario


CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def mostrar_menu():
    print()
    print(f"{CYAN}{BOLD}  🔁  MENÚ DE EJERCICIOS  🔁{RESET}")
    print()
    print(f"  {YELLOW} 1{RESET}  ☕  Peso de café")
    print(f"  {YELLOW} 2{RESET}  📦  Inventario de distribuidora")
    print(f"  {YELLOW} 3{RESET}  🏬  Ventas del minisúper")
    print(f"  {YELLOW} 4{RESET}  🥖  Producción de panadería")
    print(f"  {YELLOW} 5{RESET}  ⭐  Valoración de restaurante")
    print(f"  {YELLOW} 6{RESET}  🔐  Control de acceso")
    print(f"  {YELLOW} 7{RESET}  💰  Cierre de caja")
    print(f"  {YELLOW} 8{RESET}  🏍️   Combustible de motocicleta")
    print(f"  {YELLOW} 9{RESET}  🧾  Validar pedido")
    print(f"  {YELLOW}10{RESET}  🔄  Reposición de inventario")
    print(f"  {YELLOW}11{RESET}  🚪  Salir")
    print()


def main():
    while True:
        os.system("cls")
        mostrar_menu()

        opc = int(input(f"  {GREEN}👉 Seleccione una opción:{RESET} "))
        match opc:
            case 1:
                pesoCafe()
            case 2:
                inventarioDistribuidora()
            case 3:
                ventasMinisuper()
            case 4:
                produccionPanaderia()
            case 5:
                valoracionRestaurante()
            case 6:
                controlAcceso()
            case 7:
                cierreCaja()
            case 8:
                combustibleMotocicleta()
            case 9:
                validarPedido()
            case 10:
                reposicionInventario()
            case 11:
                print(f"\n  {GREEN}👋 ¡Hasta luego!{RESET}")
                break
            case _:
                print(f"\n  {RED}❌ Opción no válida{RESET}")

        input(f"\n  {YELLOW}⏎  Presione Enter para continuar...{RESET}")


if __name__ == "__main__":
    main()
