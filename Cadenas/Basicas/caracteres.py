cadena = input("Ingrese una cadena: ")
if len(cadena) == 0:
    print("La cadena está vacía")
else:
    print("Primer carácter:", cadena[0])
    print("Último carácter:", cadena[-1])
    print("Longitud:", len(cadena))
    print("Cadena invertida:", cadena[::-1])
