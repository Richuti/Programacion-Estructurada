
class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

    def print(self):
        print(self.key)

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, new: Node):
        if self.root == None:
            self.root = new
        else:
            if new.key > self.root.key:
                temp = self.root.right
                if temp == None:
                    temp = new
                else:
                    self.insert(temp)