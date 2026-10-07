frase = input("Ingrese una frase: ")
palabra = input("Ingrese la palabra a buscar: ")
posicion = frase.find(palabra)
if posicion == -1:
    print("La palabra no aparece en la frase")
else:
    print("La palabra aparece en la frase")
    print("Comienza en la posición:", posicion)
