class Bitree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Bitree(value)
                else:
                    self.left.add(value)

            elif value > self.value:
                if self.right is None:
                    self.right = Bitree(value)
                else:
                    self.right.add(value)

    def show(self, n=0):
        print(n * "_", self.value)
        if self.left:
            self.left.show(n + 1)
        if self.right:
            self.right.show(n + 1)


a = Bitree(100)
a.add(60)
a.add(33)
a.add(21)
a.add(150)
a.add(149)
a.add(151)
print(a.show())
