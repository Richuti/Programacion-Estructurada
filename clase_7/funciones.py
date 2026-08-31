def convertir_a_dolares(cordobas):
    tasa = 36.80
    return cordobas / tasa

monto = float(input("Monto en córdobas: "))
resultado = convertir_a_dolares(monto)
print("Equivalente en dólares:", round(resultado, 2))