from collections import defaultdict


def part1():
    with open("day5/input.txt", "r") as f:
        ranges = True
        fresh = defaultdict(int)
        cnt = 0
        collect = set()
        for line in f:
            line = line.strip()
            if not line:
                ranges = False
                continue
            if ranges:
                start, end = map(int, line.split('-'))
                fresh[start] += 1
                fresh[end+1] -= 1
            if not ranges:
                v = int(line)
                fresh[v]
                collect.add(v)
        delta = 0
        cnt = 0
        for effect in sorted(fresh):
            delta += fresh[effect]
            if delta and effect in collect:
                cnt += 1
        print(cnt)


def part2():
    with open("day5/input.txt", "r") as f:
        ranges = True
        fresh = defaultdict(int)
        cnt = 0
        collect = set()
        intervals = []
        lst = []
        for line in f:
            line = line.strip()
            if not line:break
            start, end = map(int, line.split('-'))
            lst.append((start, end))
        lst.sort()
        for start,end in lst:
            if intervals and intervals[-1][0] <= start <= intervals[-1][1]:
                intervals[-1][1] = max(intervals[-1][1], end)
            else:
                intervals.append([start, end])
        acc = 0
        for s,e in intervals:
            acc +=(e-s+1)
        print(acc)

part1()
part2()
