class Field:
    SIGNS = ' XO'

    def __init__(self, state=0, player=0):
        self.state = state
        self.player = player

    def __getitem__(self, arg):
        return self.state // 3**arg % 3

    def __repr__(self):
        return '[%s]\\n' % ']\\n['.join(
            ']['.join(self.ch(i, j) for i in range(3)) for j in range(3)
        )

    def __and__(self, other):
        return all(not other[i] or self[i] == other[i] for i in range(9))

    def ch(self, i, j):
        return Field.SIGNS[self[i + 3 * j]]

    def __add__(self, arg):
        return Field(self.state + 3**arg * (self.player + 1), not self.player)


class Indent:
    def __init__(self, out, symbol='\t'):
        self.out = out
        self.symbol = symbol
        self.indent = 0

    def parse(self, line):
        indent = self.indent if line else 0
        self.indent += line.count('{') - line.count('}')
        indent = min(self.indent, indent)
        return f'{indent*self.symbol}{line}'

    def write(self, arg):
        return self.out.write('\n'.join(self.parse(line) for line in arg.split('\n')))

    def flush(self):
        return self.out.flush()


wins = (13, 351, 9477, 757, 2271, 6813, 6643, 819)


def check(field):
    for i in (1, 2):
        if any(field & Field(state * i) for state in wins):
            return i
    return 0


def act(field, deep=0):
    print('printf("\\33c%s");' % field)
    if check(field) or deep == 9:
        print('return 0;')
        return
    print('while (1) {')
    print('switch (getc(stdin)) {')
    for i in range(9):
        if field[i]:
            continue
        print('case %d: {' % (i + ord('1')))
        act(field + i, deep + 1)
        print('}')
    print('}')
    print('}')


import sys

sys.stdout = Indent(open('tictactoe.c', 'w'))


field = Field()
print('#include <stdio.h>')
print('#include <termios.h>')
print('int main() {')
print('struct termios termios_p;')
print('tcgetattr(0, &termios_p);')
print('termios_p.c_lflag &= ~(ECHO|ICANON);')
print('tcsetattr(0, TCSANOW, &termios_p);')
act(field)
print('}')
