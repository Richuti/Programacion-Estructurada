
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

    def is_empty(self):
        return self.root is None

    def insert(self, new: Node):
        # Arbol vacio: el nuevo nodo es la raiz
        if self.root is None:
            self.root = new
            return

        current = self.root
        while True:
            # Menores o iguales a la izquierda (igual que en remove)
            if new.key <= current.key:
                if current.left is None:
                    current.left = new
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    return
                current = current.right

    def search(self, key: int):
        current = self.root
        while current and current.key != key:
            current = current.left if key <= current.key else current.right
        return current

    def minimum(self):
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current

    def maximum(self):
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current

    def remove(self, key: int):
        parent = None
        current = self.root

        # Buscar nodo
        while current and current.key != key:
            parent = current
            current = current.left if key <= current.key else current.right

        if current is None:
            return None

        removed = current

        # Buscar reemplazo si tiene dos hijos
        if current.left and current.right:
            successorParent = current
            successor = current.right

            while successor.left:
                successorParent = successor
                successor = successor.left

            if successorParent != current:
                successorParent.left = successor.right
                successor.right = current.right

            successor.left = current.left
            replacement = successor

        else:
            replacement = current.left or current.right

        # Actualizar enlace del padre o la raíz
        if parent is None:
            self.root = replacement
        elif parent.left == current:
            parent.left = replacement
        else:
            parent.right = replacement

        # Desvincular nodo eliminado
        removed.left = removed.right = None

        return removed

    # ---------- Recorridos ----------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)

    # ---------- Propiedades ----------
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def size(self):
        return len(self.inorder())


if __name__ == "__main__":
    arbol = ABB()
    for valor in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        arbol.insert(Node(valor))

    print("Inorden:  ", arbol.inorder())
    print("Preorden: ", arbol.preorder())
    print("Postorden:", arbol.postorder())
    print("Altura:", arbol.height(), "| Tamaño:", arbol.size())
    print("Minimo:", arbol.minimum().key, "| Maximo:", arbol.maximum().key)
    print("Buscar 40:", arbol.search(40) is not None)
    print("Buscar 99:", arbol.search(99) is not None)

    arbol.remove(20)   # hoja
    print("Eliminar 20 (hoja):        ", arbol.inorder())
    arbol.remove(30)   # dos hijos
    print("Eliminar 30 (dos hijos):   ", arbol.inorder())
    arbol.remove(50)   # raiz
    print("Eliminar 50 (raiz):        ", arbol.inorder())
    print("Eliminar 99 (no existe):   ", arbol.remove(99))
