from stack import Node, Stack, Product

def main():
    pila = Stack()
    prod = Product(1, "Arroz", 30, 300)
    pila.push(prod)
    prod = Product(2, "Resfresco Selva", 35, 50)
    pila.push(prod)

main()
