correo = input("Ingrese su correo: ")
posicion_arroba = correo.find("@")
if posicion_arroba == -1:
    print("Correo inválido: falta el @")
elif "." not in correo[posicion_arroba + 1:]:
    print("Correo inválido: falta un punto después del @")
else:
    print("Correo válido:", correo)
