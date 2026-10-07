palabra = input("Ingrese la palabra a contar: ")
with open("servicios.txt", "r") as archivo:
    contenido = archivo.read()
palabras = contenido.lower().split()
veces = palabras.count(palabra.lower())
print("La palabra", palabra, "aparece", veces, "veces")
