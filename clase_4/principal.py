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


def main():
    while True:
        os.system("cls")
        print("=================MENU================")
        print("1.-------------Inventario de Pulperia")
        print("2.-------------Promoción de una tienda")
        print("3.-------------Meta de ventas")
        print("4.-------------Entrega de un comedor")
        print("5.-------------Peso de productos")
        print("6.-------------Pulperia")
        print("7.-------------Entregas")
        print("8.-------------Cooperativa")
        print("9.-------------Hospedaje")
        print("10.------------Ferreteria")
        print("11.------------Salir")

        opc = int(input("Seleccione una opcion: "))
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
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")


if __name__ == "__main__":
    main()
