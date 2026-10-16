class Product:
    def __init__(self, id:int, nombre:str, precio:float, stock:int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        

class Node:
    def __init__(self, data: Product):
        self.data = data
        self.sig = None
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, new: Node):
        if self.top == None: 
            self.top = new
        else:
            new.next = self.top
            self.top = new