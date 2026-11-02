entrada = input("Ingrese los nombres separados por ;: ")
nombres = []
for nombre in entrada.split(";"):
    nombre_limpio = nombre.strip()
    if nombre_limpio != "":
        nombres.append(nombre_limpio)
print(nombres)
for nombre in nombres:
    print(nombre)
