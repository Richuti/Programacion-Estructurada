from stack import Stack, Product

def main():
    pila = Stack()
    prod = Product(1, "Arroz", 30, 300)
    pila.push(prod)
    prod = Product(2, "Resfresco Selva", 35, 50)
    pila.push(prod)
    productos = pila.clear()
    for p in productos:
        p.print()
    

main()
