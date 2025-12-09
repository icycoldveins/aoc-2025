from itertools import combinations


def part1():
    points = []
    with open('day9/input.txt', 'r') as f:
        for line in f:
            line=line.strip()
            i,j = map(int,line.split(','))
            points.append((i,j))
        mx = 0
        n = len(points)

        print(points)

        def getarea(c1, c2):
            x1, y1 = c1
            x2, y2 = c2
            l = abs(x1-x2)+1
            w = abs(y1-y2)+1
            return l*w
        for i, j in combinations(range(n), 2):
            mx = max(mx, getarea(points[i], points[j]))
        print(mx)


part1()
