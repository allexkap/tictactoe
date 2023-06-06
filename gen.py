class Field:

    SIGNS = ' XO'

    def __init__(self, state=0):
        self.state = state

    def __getitem__(self, arg):
        return self.state // 3**arg % 3

    def __str__(self):
        return '[%s]\n' % ']\n['.join(']['.join(self.ch(i, j) for i in range(3)) for j in range(3))

    def ch(self, i, j):
        return Field.SIGNS[self[i + 3*j]]
