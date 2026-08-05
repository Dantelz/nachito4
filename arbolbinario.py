from collections import deque
from platform import node

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inorder(self, nodo=None, resultado=None):
        if resultado is None:
            resultado = []
            nodo = self.raiz
        if nodo is None:
            return resultado
        self.inorder(nodo.izquierdo, resultado)
        resultado.append(nodo.valor)
        self.inorder(nodo.derecho, resultado)
        return resultado

    def preorder(self, nodo=None, resultado=None):
        if resultado is None:
            resultado = []
            nodo = self.raiz
        if nodo is None:
            return resultado
        resultado.append(nodo.valor)
        self.preorder(nodo.izquierdo, resultado)
        self.preorder(nodo.derecho, resultado)
        return resultado

    def postorder(self, nodo=None, resultado=None):
        if resultado is None:
            resultado = []
            nodo = self.raiz
        if nodo is None:
            return resultado
        self.postorder(nodo.izquierdo, resultado)
        self.postorder(nodo.derecho, resultado)
        resultado.append(nodo.valor)
        return resultado


if __name__ == "__main__":
    raiz = Nodo("A")
    raiz.izquierdo = Nodo("B")
    raiz.derecho = Nodo("C")
    raiz.izquierdo.izquierdo = Nodo("D")
    raiz.izquierdo.derecho = Nodo("E")
    raiz.derecho.derecho = Nodo("F")
    raiz.izquierdo.izquierdo.izquierdo = Nodo("G")
    raiz.izquierdo.izquierdo.derecho = Nodo("H")

    arbol = ArbolBinario(raiz)
    print("Recorrido In Order:", arbol.inorder())
    print("Recorrido Pre Order:", arbol.preorder())
    print("Recorrido Post Order:", arbol.postorder())


def level_order(raiz):
    list = []
    queue = deque()
    while len(queue) > 0:
            current = queue.popleft()
            list.append(current.valor)
            if current.izquierdo is not None:
                queue.append(current.izquierdo)
            if current.derecho is not None:
                queue.append(current.derecho)
    return list

def main():
    level_order(raiz)
    print("Recorrido Level Order:", level_order(raiz))

main()