lista1 = ["Maria", "Juan", "Pedro"]
lista2 = [[89.23, "72"], [56, 99]]
lista3 = [[23.6, 45.6, 67.8]]
concat = lista1 + lista2 + lista3

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print(dias)
del dias[2]
print(dias)


precios = [100, 200, 300, 400, 500]

print(precios)

def actualizarprecios(precios):
    for i in range(0, precios.count()):
        precios[i] = precios[i] * 1.1
    return precios

print(actualizarprecios(precios))





