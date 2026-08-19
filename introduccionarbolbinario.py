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


def inverse_polish_parser(expresion):
    stack = []

    for elemento in expresion.split():
        if elemento not in "+-*/":
            stack.append(Nodo(elemento))
        else:
            derecho = stack.pop()
            izquierdo = stack.pop()

            nodo = Nodo(elemento)
            nodo.izquierdo = izquierdo
            nodo.derecho = derecho

            stack.append(nodo)

    return stack.pop()


def calculate(nodo):
    if nodo.izquierdo is None and nodo.derecho is None:
        return float(nodo.valor)

    izquierdo = calculate(nodo.izquierdo)
    derecho = calculate(nodo.derecho)

    if nodo.valor == "+":
        return izquierdo + derecho
    elif nodo.valor == "-":
        return izquierdo - derecho
    elif nodo.valor == "*":
        return izquierdo * derecho
    elif nodo.valor == "/":
        return izquierdo / derecho


def evaluate(expresion):
    arbol = inverse_polish_parser(expresion)
    return calculate(arbol)


def level_order(raiz):
    lista = []
    queue = deque()

    if raiz is not None:
        queue.append(raiz)

    while len(queue) > 0:
        current = queue.popleft()
        lista.append(current.valor)

        if current.izquierdo is not None:
            queue.append(current.izquierdo)

        if current.derecho is not None:
            queue.append(current.derecho)

    return lista


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
    print("Resultado:", calculate(arbol.raiz))
    print("Evaluate:", evaluate("2 6 + 8 / 9 2 - *"))
    print("Recorrido Level Order:", level_order(raiz))