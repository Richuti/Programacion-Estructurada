nombres = ["Ana", "Luis", "Maria"]
edades = [20, 25, 22]
ciudades = ["Caracas", "Valencia", "Maracaibo"]
usuarios = []
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    usuarios.append(usuario)
print(usuarios)
for usuario in usuarios:
    print(usuario)
