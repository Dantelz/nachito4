class nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = nodo(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = nodo(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        else:
            if self.right is None:
                return False
            return self.right.search(value)

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
        elements.append(self.value)
        if self.right:
            elements += self.right.in_order()
        return elements


class bst:
    def __init__(self, value=None):
        self.root = nodo(value) if value is not None else None

    def insert(self, value):
        if self.root is None:
            self.root = nodo(value)
        else:
            self.root.insert(value)

    def search(self, value):
        if self.root is None:
            return False
        return self.root.search(value)

    def get_max(self):
        if self.root is None:
            return None
        return self.root.get_max()

    def get_min(self):
        if self.root is None:
            return None
        return self.root.get_min()

    def in_order(self):
        if self.root is None:
            return []
        return self.root.in_order()

def main():
    tree = bst(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)

    print("In-order:", tree.in_order())
    print("Search 7:", tree.search(7))
    print("Search 20:", tree.search(20))
    print("Max value:", tree.get_max())
    print("Min value:", tree.get_min())


main()

