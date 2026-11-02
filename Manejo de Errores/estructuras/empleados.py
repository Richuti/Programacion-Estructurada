import os

def diccionarioEmpleados():
    os.system("cls")

    empleados = {
        "001": "Ana Lopez",
        "002": "Carlos Ruiz",
        "003": "Maria Perez"
    }

    codigo = input("Ingrese el codigo del empleado: ")

    try:
        print(f"El empleado es: {empleados[codigo]}")
    except KeyError:
        print("Error: ese codigo de empleado no existe")

    empleado = empleados.get(codigo, "No encontrado")
    print(f"Con get() el resultado es: {empleado}")

if __name__ == "__main__":
    diccionarioEmpleados()
