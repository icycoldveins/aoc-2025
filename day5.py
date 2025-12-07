from collections import defaultdict


def part1():
    with open("day5/input.txt", "r") as f:
        ranges = True
        rotten = defaultdict(list)
        cnt = 0
        collect = list()
        for line in f:
            line = line.strip()
            if not line:
                ranges = False
                continue
            if ranges:
                start, end = map(int, line.split('-'))
                rotten[start] = 1
                rotten[end+1] = -1

            if not ranges:
                rotten[w := int(line)] = 2
        delta = 0
        print(rotten)
        for effect in sorted(rotten):
            if (change := rotten[effect]) != 2:
                delta += change
            if not delta and rotten[effect] == 2:
                cnt += 1
        return cnt


print(part1())
