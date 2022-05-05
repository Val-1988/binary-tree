class Node:
    def __init__(self, value):
        self.value = value
        self.left_leaf = None
        self.right_leaf = None

    def add_child(self, value):
        if value < self.value:
            if self.left_leaf:
                self.left_leaf.add_child(value)
            else:
                self.left_leaf = Node(value)
        elif value > self.value:
            if self.right_leaf:
                self.right_leaf.add_child(value)
            else:
                self.right_leaf = Node(value)

    def show(self, n=0):
        print("-" * n, self.value)
        if self.left_leaf:
            self.left_leaf.show(n + 1)
        if self.right_leaf:
            self.right_leaf.show(n + 1)


class Tree:

    def __init__(self, value):
        self.node = Node(value)

    def add(self, value):
        self.node.add_child(value)

    def show(self):
        self.node.show()


a = Tree(100)
a.add(90)
a.add(120)
a.add(80)
a.add(50)
a.add(30)
a.show()
