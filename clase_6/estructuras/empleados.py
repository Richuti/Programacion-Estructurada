import os

def diccionarioEmpleados():
    os.system("cls")

    empleados = {
        "001": "Ana Lopez",
        "002": "Carlos Ruiz",
        "003": "Maria Perez"
    }

    codigo = input("Ingrese el codigo del empleado: ")

    # Acceso directo: lanza KeyError si la clave no existe
    try:
        print(f"El empleado es: {empleados[codigo]}")
    except KeyError:
        print("Error: ese codigo de empleado no existe")

    # Alternativa con get(): no lanza excepcion, devuelve un valor por defecto
    empleado = empleados.get(codigo, "No encontrado")
    print(f"Con get() el resultado es: {empleado}")

if __name__ == "__main__":
    diccionarioEmpleados()
