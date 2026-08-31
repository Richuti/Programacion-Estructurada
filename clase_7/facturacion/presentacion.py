def mostrar_factura(producto, cantidad, subtotal, impuesto, total):
    print()
    print("--------- FACTURA ---------")
    print(f"Producto:  {producto}")
    print(f"Cantidad:  {cantidad}")
    print(f"Subtotal:  C$ {round(subtotal, 2)}")
    print(f"IVA:       C$ {round(impuesto, 2)}")
    print(f"Total:     C$ {round(total, 2)}")
    print("---------------------------")


def mostrar_error(mensaje):
    print(f"Error: {mensaje}")
