import os

from retos.comision import probar_comision
from retos.cafe import probar_cafe
from retos.entrega import probar_entrega
from retos.resumen import probar_resumen
from retos.inventario import probar_inventario
from retos.moneda import probar_moneda
from retos.nota import probar_nota
from facturacion.factura import facturacion_modular


CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def mostrar_menu():
    print()
    print(f"{CYAN}{BOLD}  🧩  RETOS CONTEXTUALIZADOS  🧩{RESET}")
    print()
    print(f"  {YELLOW}1{RESET}  💵  Comisión de ventas")
    print(f"  {YELLOW}2{RESET}  ☕  Clasificación de café")
    print(f"  {YELLOW}3{RESET}  🚚  Tarifa de entrega")
    print(f"  {YELLOW}4{RESET}  📈  Resumen semanal")
    print(f"  {YELLOW}5{RESET}  📦  Inventario mínimo")
    print(f"  {YELLOW}6{RESET}  💱  Conversión de moneda")
    print(f"  {YELLOW}7{RESET}  🎓  Nota final")
    print(f"  {YELLOW}8{RESET}  🧾  Facturación modular")
    print(f"  {YELLOW}9{RESET}  🚪  Salir")
    print()


def main():
    while True:
        os.system("cls")
        mostrar_menu()

        opc = int(input(f"  {GREEN}👉 Seleccione una opción:{RESET} "))
        match opc:
            case 1:
                probar_comision()
            case 2:
                probar_cafe()
            case 3:
                probar_entrega()
            case 4:
                probar_resumen()
            case 5:
                probar_inventario()
            case 6:
                probar_moneda()
            case 7:
                probar_nota()
            case 8:
                facturacion_modular()
            case 9:
                print(f"\n  {GREEN}👋 ¡Hasta luego!{RESET}")
                break
            case _:
                print(f"\n  {RED}❌ Opción no válida{RESET}")

        input(f"\n  {YELLOW}⏎  Presione Enter para continuar...{RESET}")


if __name__ == "__main__":
    main()
