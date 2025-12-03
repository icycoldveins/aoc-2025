'''
--- Day 3: Lobby ---
'''
from functools import cache


def part1():
    def fn(s):
        max_r = best = ""
        for ch in reversed(s):
            if max_r: best = max(best, ch+max_r)
            max_r = max(max_r, ch)
        return best
    cnt = 0
    with open('day3/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            cnt += int(fn(line))
    return cnt


def part2():
    def fn(s):
        @cache
        def dp(i, left):
            if i == len(s):
                return ""
            if not left:
                return ""
            # take
            take = ""
            if left:
                take = s[i]+dp(i+1, left-1)
            # skip
            skip = dp(i+1, left)

            return max(skip, take, key=lambda x: (len(x), x))
        return dp(0, 3)

    cnt = 0
    with open('day3/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            cnt += int(w:=fn(line))
            print(w)
    return cnt


print(part2())
