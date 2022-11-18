from OOPsPython import Parent


class ChildClass(Parent):

    c = 100

    def __init__(self, p, q):
        self.c1 = p
        self.c2 = q
        Parent.__init__(self, 200, 300)

    def subaddition(self):
        return self.c + self.c1 + self.c2 + self.addition()


obj = ChildClass(100, 100)
print(obj.subaddition())
