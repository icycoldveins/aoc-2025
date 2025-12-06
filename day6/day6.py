from collections import defaultdict
from functools import reduce
import operator


def part1():
    levels = defaultdict(list)
    operation = {
        '+': operator.add,
        '*': operator.mul
    }
    with open('day6/input.txt', 'r') as f:
        for line in f:
            line = line.split()
            for i, v in enumerate(line):
                try:
                    levels[i].append(int(v))
                except ValueError:
                    levels[i].append(v)

    ans = 0
    for level in levels:
        lst = levels[level]
        ans += reduce(operation[lst[-1]], lst[:-1])

    print(ans)


'''
need to group cols right to left together 
'''


def part2():
    operation = {
        '+': operator.add,
        '*': operator.mul
    }
    with open('day6/input.txt', 'r') as f:
        collect = [line[:-1] for line in f]
        maxcol = max(len(line) for line in collect)
        col = maxcol - 1
        temp = ""
        calc = []
        ans = 0
        while col >= 0:
            for line in collect:
                if col >= len(line):
                    continue
                v = line[col]
                if v in {'*', '+'}:
                    calc.append(int(temp))
                    ans += reduce(operation[v], calc)
                    temp = ""
                    calc = []
                elif v == ' ':
                    continue
                else:
                    temp += v
            if temp:
                calc.append(int(temp))
                temp = ""
            col -= 1
        print(ans)

part1()
part2()

