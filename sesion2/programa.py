# Autor: Richard Diaz
nombre = input("Ingrese el nombre del estudiante: ")
calificacion = float(input("Ingrese la calificación obtenida (0 a 100): "))

if calificacion >= 60 and calificacion <= 89.99:
    resultado = "Aprobado"
elif calificacion >= 90 and calificacion <= 100:
    resultado = "Excelente"
else:
    resultado = "Reprobado"

print(f"{nombre}: {resultado} con una calificación de {calificacion:.1f}")