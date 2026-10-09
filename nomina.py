import os


empleado = {
    "id": "",
    "nombre": "",
    "salario": 0.0,
    "antiguedad": 0,
    "departamento": "",
}

nomina = []

def agregar_empleado():
    print("******REGISTRO DE EMPLEADOS******")
    empleado["id"] = input("Ingrese el ID del empleado: ")
    empleado["nombre"] = input("Ingrese el nombre del empleado: ")
    empleado["salario"] = float(input("Ingrese el salario del empleado: "))
    empleado["antiguedad"] = int(input("Ingrese la antiguedad del empleado: "))
    empleado["departamento"] = input("Ingrese el departamento del empleado: ")
    nomina.append(empleado.copy())

def buscar_empleado(id:str) -> int:
    encontrado = None
    for emp in range(0, len(nomina)):
        if nomina[emp]["id"] == id:
            encontrado = emp
            break
    return encontrado

def eliminar_empleado(id:str) -> bool:
    '''La Funcion retorna True en caso de eliminacion, de lo contrario retorna False'''
    index = buscar_empleado(id)
    if index != None:
        nomina.pop(index)
        return True
    return False

def actualizar_empleado(id:str) -> bool:
    '''La Funcion retorna True en caso de actualizacion, de lo contrario retorna False'''
    index = buscar_empleado(id)
    if index != None:
        print("---- Seleccione el campo a actualizar ----")
        print("1. Nombre")
        print("2. Salario")
        print("3. Antiguedad")
        print("4. Departamento")
        print("5. Salir")
        opcion = int(input("Ingrese la opcion: "))
        match opcion:
            case 1: 
                nomina[index]["nombre"] = input("Ingrese el nombre del empleado: ")
            case 2:
                nomina[index]["salario"] = float(input("Ingrese el salario del empleado: "))
            case 3:
                nomina[index]["antiguedad"] = int(input("Ingrese la antiguedad del empleado: "))
            case 4:
                nomina[index]["departamento"] = input("Ingrese el departamento del empleado: ")
            case 5:
                print("Exito al actualizar el empleado")
            case _:
                print("Opcion no valida")
        return True
    return False

def guardar_nomina():
    fichero_empleado = open("nomina.txt", "w", encoding="utf-8")
    for emp in nomina:
        fichero_empleado.write(emp["id"] + ",")
        fichero_empleado.write(emp["nombre"] + ",")
        fichero_empleado.write(str(emp["salario"]) + ",")
        fichero_empleado.write(str(emp["antiguedad"]) + ",")
        fichero_empleado.write(emp["departamento"] + "\n")
    fichero_empleado.close()

def cargar_nomina() -> int:
    campo = None
    reg = None
    cant = 0
    fichero_empleado = open("nomina.txt", "r", encoding="utf-8")
    fichero_empleado.seek(0, os.SEEK_END)
    reg = fichero_empleado.tell()
    if reg != 0:
        fichero_empleado.seek(0, os.SEEK_SET)
        campo = fichero_empleado.readline()
        while campo != "":
            if campo.strip() != "":
                datos = campo.rstrip("\n").split(",")
                emp = {}
                emp["id"] = datos[0]
                emp["nombre"] = datos[1]
                emp["salario"] = float(datos[2])
                emp["antiguedad"] = int(datos[3])
                emp["departamento"] = datos[4]
                nomina.append(emp)
                cant += 1
            campo = fichero_empleado.readline()
    fichero_empleado.close()
    return cant
