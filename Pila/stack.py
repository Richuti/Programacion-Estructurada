class Product:
    def __init__(self, id:int, nombre:str, precio:float, stock:int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.next = None

    def print(self):
        print(f"[ID: {self.id} | Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}]")    
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, new: Product):
        if self.top == None: 
            self.top = new
        else:
            new.next = self.top
            self.top = new

    def pop(self) -> Product:
        prod = self.top
        if not self.isEmpty():
            prod = self.top
            if self.top.next != None:
                self.top = self.top.next
            else:
                self.top = None
        return prod

    def isEmpty(self) -> bool:
        if self.top == None:
            return True
        else:
            return False

