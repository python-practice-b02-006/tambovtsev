class UEpsilon(set):
    def __init__(self, epsilon, lst):
        super().__init__(lst)
        self.epsilon = epsilon

    def add(self, x, epsilon):
        if all(map(lambda x0: abs(x - x0) >= self.epsilon, self)):
            super().add(x)


a = UEpsilon(1, [1, 2, 3])
print(*a)
a.add(10, 1)
print(*a)
a.add(3.5, 1)
print(*a)