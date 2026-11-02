proveedor_a = {"laptop", "mouse", "teclado", "monitor", "impresora"}
proveedor_b = {"mouse", "parlantes", "monitor", "camara", "teclado"}
catalogo = proveedor_a | proveedor_b
print("Proveedor A:", proveedor_a)
print("Proveedor B:", proveedor_b)
print("Catalogo final:", catalogo)
print("Total de productos:", len(catalogo))