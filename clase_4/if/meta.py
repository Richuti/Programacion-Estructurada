import os
os.system("cls")

meta_diaria = 4000
vendido = float(input("Ingreses el total vendido: "))

if vendido < meta_diaria:
    faltante = meta_diaria - vendido
    print(f"Todavia falta {faltante} para completar el objetivo diario")
else:
    sobrante = vendido - meta_diaria
    print(f"Ya completaste el objetivo diario y te superaste por {sobrante}") 