def resumen_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    maxima = max(ventas)
    return total, promedio, maxima


ventas = [100, 200, 300, 400, 500, 600, 700]
resultado = resumen_ventas(ventas)
print(resultado)
total, promedio, maxima = resultado
print("Total:", total)
print("Promedio:", promedio)
print("Venta máxima:", maxima)
