import os

def registroEmpleado():
    os.system("cls")

    nombre = input("Ingrese su nombre: ")

    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Error: debe corregir la edad, tiene que ser un numero entero")
        return

    try:
        salario = float(input("Ingrese su salario: "))
    except ValueError:
        print("Error: debe corregir el salario, tiene que ser un valor numerico")
        return

    print(f"Empleado: {nombre}")
    print(f"Edad: {edad}")
    print(f"Salario: {salario}")

if __name__ == "__main__":
    registroEmpleado()
