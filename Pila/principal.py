from stack import Node, Stack, Product

def main():
    pila = Stack()
    prod = Product(1, "Arroz", 30, 2)
    nodo = Node(prod)
    pila.push(nodo)
    
main()
