class Field:

    SIGNS = ' XO'

    def __init__(self, state=0, player=0):
        self.state = state
        self.player = player

    def __getitem__(self, arg):
        return self.state // 3**arg % 3

    def __repr__(self):
        return '[%s]\\n' % ']\\n['.join(']['.join(self.ch(i, j) for i in range(3)) for j in range(3))

    def __and__(self, other):
        return all(not other[i] or self[i] == other[i] for i in range(9))

    def ch(self, i, j):
        return Field.SIGNS[self[i + 3*j]]

    def __add__(self, arg):
        return Field(self.state + 3**arg * (self.player+1), not self.player)


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
    print('value = getc(stdin) - \'0\';')
    for i in range(9):
        if field[i]: continue
        print('if (value == %d) {' % (i+1))
        act(field + i, deep+1)
        print('}')
    print('}')



import sys
sys.stdout = open('auto.c', 'w')

indent = 0
_print = print
def print(*args, **kwargs):
    if len(args) != 1:
        _print(*args, **kwargs)
        return
    global indent
    indent -= args[0].count('}')
    _print('\t' * indent, end='')
    _print(*args, **kwargs)
    indent += args[0].count('{')


field = Field()
print('#include <stdio.h>')
print('#include <termios.h>')
print('int main() {')
print('struct termios termios_p;')
print('tcgetattr(0, &termios_p);')
print('termios_p.c_lflag &= ~(ECHO|ICANON);')
print('tcsetattr(0, TCSANOW, &termios_p);')
print('int value;')
act(field)
print('}')
