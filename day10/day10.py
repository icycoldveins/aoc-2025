from functools import cache
from math import inf


def part1():
    lst = []
    with open('day10/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            lst.append(line.split(' '))

    total = 0
    for line in lst:
        diagram = line[0][1:-1]
        target = 0
        for i, ch in enumerate(diagram):
            if ch == '#':
                target |= (1 << i)

        button_strs = line[1:-1]
        buttons = []

        for b in button_strs:
            mask = 0
            for x in b[1:-1].split(','):
                mask |= (1 << int(x))
            buttons.append(mask)

        n = len(buttons)

        @cache
        def dp(idx, state):
            if idx == n:
                return 0 if state == target else inf
            skip = dp(idx + 1, state)
            press = 1 + dp(idx + 1, state ^ buttons[idx])
            return min(skip, press)
        
        result = dp(0, 0)
        total += result

    print(total)

def part2():
    from z3 import Optimize, Int, Sum

    lst = []
    with open('day10/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            lst.append(line.split(' '))

    total = 0
    for line in lst:
        target = [int(x) for x in line[-1][1:-1].split(',')]
        button_strs = line[1:-1]

        buttons = []
        for b in button_strs:
            indices = [int(x) for x in b[1:-1].split(',')]
            mask = [1 if i in indices else 0 for i in range(len(target))]
            buttons.append(mask)

        opt = Optimize()
        vv = []

        for i in range(len(buttons)):
            v = Int(f"v_{i}")
            vv.append(v)
            opt.add(v >= 0)

        for j in range(len(target)):
            opt.add(Sum([buttons[i][j] * vv[i] for i in range(len(buttons))]) == target[j])

        opt.minimize(Sum(vv))
        opt.check()

        m = opt.model()
        result = sum(m[v].as_long() for v in vv)
        total += result

    print(total)


part1()
part2()
