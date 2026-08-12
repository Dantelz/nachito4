from collections import deque


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

    def level_order(self):
        resultado = []
        cola = deque()

        if self.raiz is not None:
            cola.append(self.raiz)

        while len(cola) > 0:
            actual = cola.popleft()
            resultado.append(actual.valor)

            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)

            if actual.derecho is not None:
                cola.append(actual.derecho)

        return resultado


if __name__ == "__main__":

    raiz = Nodo("*")
    raiz.izquierdo = Nodo("/")
    raiz.izquierdo.izquierdo = Nodo("+")
    raiz.izquierdo.derecho = Nodo("8")
    raiz.izquierdo.izquierdo.izquierdo = Nodo("2")
    raiz.izquierdo.izquierdo.derecho = Nodo("6")
    raiz.derecho = Nodo("-")
    raiz.derecho.izquierdo = Nodo("9")
    raiz.derecho.derecho = Nodo("2")

    arbol = ArbolBinario(raiz)

    print("Recorrido In Order:", arbol.inorder())
    print("Recorrido Pre Order:", arbol.preorder())
    print("Recorrido Post Order:", arbol.postorder())
    print("Recorrido Level Order:", arbol.level_order())