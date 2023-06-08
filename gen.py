class Field:

    SIGNS = ' XO'

    def __init__(self, state=0, offset=0):
        self.state = state
        self.offset = offset

    def __getitem__(self, arg):
        return self.state // 3**arg % 3

    def __repr__(self):
        return '[%s]\\n' % ']\\n['.join(']['.join(self.ch(i, j) for i in range(3)) for j in range(3))

    def __and__(self, other):
        return all(not other[i] or self[i] == other[i] for i in range(9))

    def ch(self, i, j):
        return Field.SIGNS[self[i + 3*j]]

    def __add__(self, arg):
        return Field(self.state + 3**arg * (self.offset+1), not self.offset)


wins = (13, 351, 9477, 757, 2271, 6813, 6643, 819)
def check(field):
    for i in (1, 2):
        if any(field & Field(state*i) for state in wins):
            return i
    return 0


def act(field, deep=0):
    print('printf("\\33c%s");' % field)
    if c := check(field):
        print('return 0;')
        return
    if deep == 9:
        print('return 0;')
        return
    print('while (1) {')
    print('scanf("%d", &value);')
    for i in range(9):
        if field[i]: continue
        print('if (value == %d) {' % (i+1))
        act(field + i, deep+1)
        print('}')
    print('printf("\\33[1A\\33[K");')
    print('}')



import sys
sys.stdout = open('auto.c', 'w')

field = Field()
print('#include <stdio.h>\nint main() {\nint value;')
act(field)
print('}')
