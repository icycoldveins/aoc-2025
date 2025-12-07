from collections import defaultdict
from functools import cache


def part1():
    splits = set()
    cnt=0
    with open('day7/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            for i, char in enumerate(line):
                if char == 'S':
                    splits.add(i)
                elif char == '^' and i in splits:
                    cnt+=1
                    splits.remove(i)
                    splits.add(i-1)
                    splits.add(i+1)
        print(cnt)
def part2():
    splits = set()
    coalesce = []
    cnt=0
    with open('day7/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            coalesce.append(line)
    n = len(coalesce)
    m = len(coalesce[0])
    @cache
    def dp(i,j):
        if i == n:
            return 1
        ret = 0
        if coalesce[i][j] == '^':
            ret += dp(i+1,j-1)
            ret += dp(i+1,j+1)
        else:
            ret = dp(i+1,j)
        return ret 
    for j in range(m):
        if coalesce[0][j] == 'S':
            print(dp(0,j))
part1()
part2()



