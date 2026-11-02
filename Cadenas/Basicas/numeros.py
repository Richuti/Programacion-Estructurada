codigo = input("Ingrese el código: ")
if codigo.isdigit():
    numero = int(codigo)
    print("El código solo tiene dígitos")
    print("Convertido a entero:", numero)
else:
    print("El código tiene caracteres que no son dígitos")
