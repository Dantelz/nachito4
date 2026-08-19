class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):     
        nodo = Node(data)
        if self.root is None:
            self.root = nodo
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = nodo
                    return
                else:
                    current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = nodo
                    return
                else:
                    current = current.right
            else:
                return  
    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return True

            elif data < current.data:
                current = current.left

            else:
                current = current.right

        return False

    def in_order(self):
        resultado = []
        self._in_order(self.root, resultado)
        return resultado

    def _in_order(self, nodo, resultado):
        if nodo is not None:
            self._in_order(nodo.left, resultado)
            resultado.append(nodo.data)
            self._in_order(nodo.right, resultado)

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def remove(self, data):
        self.root = self._remove(self.root, data)

    def _remove(self, nodo, data):
        if nodo is None:
            return None
        elif data < nodo.data:
            nodo.left = self._remove(nodo.left, data)
        elif data > nodo.data:
            nodo.right = self._remove(nodo.right, data)
        else:
            if nodo.left is None and nodo.right is None:
                return None
            if nodo.left is None:
                return nodo.right
            if nodo.right is None:
                return nodo.left

            minimo = self._find_min_node(nodo.right)
            nodo.data = minimo.data
            nodo.right = self._remove(nodo.right, minimo.data)

        return nodo

    def _find_min_node(self, nodo):
        current = nodo
        while current.left is not None:
            current = current.left
        return current


def main():
    arbol = BST()
    arbol.insert(50)
    arbol.insert(30)
    arbol.insert(70)
    arbol.insert(20)
    arbol.insert(40)
    arbol.insert(60)
    arbol.insert(80)

    print("¿Está el 40?", arbol.search(40))
    print(f"¿Está el 100? {arbol.search(100)} \n")
    print("In-order:", arbol.in_order())
    print(f"Mínimo: {arbol.find_min()}\n")
    print(f"Máximo: {arbol.find_max()}\n")

    print("Antes de eliminar:", arbol.in_order())
    arbol.remove(20)
    print("Después de eliminar 20:", arbol.in_order())
    arbol.remove(30)
    print("Después de eliminar 30:", arbol.in_order())
    arbol.remove(50)
    print("Después de eliminar 50:", arbol.in_order())


main()