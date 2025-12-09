from itertools import combinations


def getarea(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def part1():
    points = []
    with open('day9/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            i, j = map(int, line.split(','))
            points.append((i, j))

    mx = 0
    for i, j in combinations(range(len(points)), 2):
        mx = max(mx, getarea(points[i], points[j]))
    print(mx)


def part2():
    points = []
    with open('day9/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            i, j = map(int, line.split(','))
            points.append((i, j))

    n = len(points)
    cols = sorted(set(c for c, _ in points))
    rows = sorted(set(r for _, r in points))
    col_map = {c: 2 * i + 1 for i, c in enumerate(cols)}
    row_map = {r: 2 * i + 1 for i, r in enumerate(rows)}

    C, R = 2 * len(cols) + 2, 2 * len(rows) + 2
    grid = [['.'] * R for _ in range(C)]

    for i in range(n):
        p1, p2 = points[i], points[(i + 1) % n]
        c1, r1 = col_map[p1[0]], row_map[p1[1]]
        c2, r2 = col_map[p2[0]], row_map[p2[1]]
        for c in range(min(c1, c2), max(c1, c2) + 1):
            for r in range(min(r1, r2), max(r1, r2) + 1):
                grid[c][r] = '#'

    stack = [(0, 0)]
    grid[0][0] = 'X'
    while stack:
        c, r = stack.pop()
        for nc, nr in [(c+1, r), (c-1, r), (c, r+1), (c, r-1)]:
            if 0 <= nc < C and 0 <= nr < R and grid[nc][nr] == '.':
                grid[nc][nr] = 'X'
                stack.append((nc, nr))

    mx = 0
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            c1, r1 = col_map[p1[0]], row_map[p1[1]]
            c2, r2 = col_map[p2[0]], row_map[p2[1]]
            valid = all(grid[c][r] != 'X'
                        for c in range(min(c1, c2), max(c1, c2) + 1)
                        for r in range(min(r1, r2), max(r1, r2) + 1))
            if valid:
                mx = max(mx, getarea(p1, p2))
    print(mx)


part1()
part2()
