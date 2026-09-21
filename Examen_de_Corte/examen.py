import os


def main():
    mensaje = "Sistema de Cálculo de Salario"
    nombre = ""
    salario_basico = 0.0
    tasa_inss = 0.07
    tasa_vivienda = 0.10
    tasa_deduccion = 0.10
    inss = vivienda = deduccion = total_deducciones = salario_neto = 0.0

    nombre, salario_basico = leer_datos(mensaje)

    inss, vivienda, deduccion, total_deducciones, salario_neto = calcular_salario(
        salario_basico, tasa_inss, tasa_vivienda, tasa_deduccion
    )

    mostrar_resultados(nombre, salario_basico, inss, vivienda, deduccion,
                       total_deducciones, salario_neto)


def leer_datos(mensaje):
    nombre = leer_nombre(mensaje)
    salario_basico = leer_salario()
    return nombre, salario_basico


def leer_nombre(mensaje):
    os.system("cls")
    print(mensaje)
    print("*" * 40)
    nombre = ""
    while nombre == "":
        nombre = input("Ingrese el nombre del empleado: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
    return nombre


def leer_salario():
    salario_basico = 0.0
    while salario_basico <= 0:
        try:
            salario_basico = float(input("Ingrese el salario básico (C$): "))
            if salario_basico != salario_basico or salario_basico == float("inf"):
                print("Error: ingrese un número válido.")
                salario_basico = 0.0
            elif salario_basico <= 0:
                print("Error: el salario debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese un número válido.")
            salario_basico = 0.0
    return salario_basico


def calcular_salario(salario_basico, tasa_inss, tasa_vivienda, tasa_deduccion):
    inss, vivienda, deduccion, total_deducciones = calcular_deducciones(
        salario_basico, tasa_inss, tasa_vivienda, tasa_deduccion
    )
    salario_neto = calcular_neto(salario_basico, total_deducciones)
    return inss, vivienda, deduccion, total_deducciones, salario_neto


def calcular_deducciones(salario_basico, tasa_inss, tasa_vivienda, tasa_deduccion):
    inss = calcular_inss(salario_basico, tasa_inss)
    vivienda = calcular_vivienda(salario_basico, tasa_vivienda)
    deduccion = calcular_deduccion(salario_basico, tasa_deduccion)
    total_deducciones = inss + vivienda + deduccion
    return inss, vivienda, deduccion, total_deducciones


def calcular_inss(salario_basico, tasa_inss):
    inss = salario_basico * tasa_inss
    return inss


def calcular_vivienda(salario_basico, tasa_vivienda):
    vivienda = salario_basico * tasa_vivienda
    return vivienda


def calcular_deduccion(salario_basico, tasa_deduccion):
    deduccion = salario_basico * tasa_deduccion
    return deduccion


def calcular_neto(salario_basico, total_deducciones):
    salario_neto = salario_basico - total_deducciones
    return salario_neto


def mostrar_resultados(nombre, salario_basico, inss, vivienda, deduccion,
                       total_deducciones, salario_neto):
    os.system("cls")
    print("*" * 50)
    print("Comprobante de Pago".center(50))
    print("*" * 50)
    print(f"Empleado: {nombre}")
    print("-" * 50)
    print(f"{'Salario básico:':<25}C$ {salario_basico:>18,.2f}")
    print(f"{'INSS (7%):':<25}C$ {inss:>18,.2f}")
    print(f"{'Vivienda (10%):':<25}C$ {vivienda:>18,.2f}")
    print(f"{'Deducción (10%):':<25}C$ {deduccion:>18,.2f}")
    print("-" * 50)
    print(f"{'Total deducciones:':<25}C$ {total_deducciones:>18,.2f}")
    print(f"{'Salario neto:':<25}C$ {salario_neto:>18,.2f}")
    print("*" * 50)


try:
    main()
except KeyboardInterrupt:
    print("\nPrograma cancelado por el usuario.")