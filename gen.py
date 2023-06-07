class Field:

    SIGNS = ' XO'

    def __init__(self, state=0):
        self.state = state

    def __getitem__(self, arg):
        return self.state // 3**arg % 3

    def __repr__(self):
        return '[%s]\\n' % ']\\n['.join(']['.join(self.ch(i, j) for i in range(3)) for j in range(3))

    def __and__(self, other):
        return all(not other[i] or self[i] == other[i] for i in range(9))

    def ch(self, i, j):
        return Field.SIGNS[self[i + 3*j]]

    def add(self, arg, offset=1):
        return Field(self.state + 3**arg * offset)


wins = (13, 351, 9477, 757, 2271, 6813, 6643, 819)
def check(field):
    for i in (1, 2):
        if any(field & Field(state*i) for state in wins):
            return i
    return 0


def act(field, deep=0):
    if deep == 6: return
    print('printf("\33c%s");' % field)
    if c := check(field):
        print('return 0;')
        return
    print('scanf("%d", &value);')
    print('switch (value) {')
    for i in range(9):
        if field[i]: continue
        print(f'case {i+1}:')
        act(field.add(i, deep%2+1), deep+1)
        print('break;')
    print('default:')
    print('return 1;')
    print('}')



import sys
sys.stdout = open('auto.c', 'w')

field = Field()
print('#include <stdio.h>\nint main() {\nint value;')
act(field)
print('return 2;\n}')
