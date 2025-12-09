from functools import reduce
from itertools import combinations
import operator


def part1():
    points = []
    with open('day8/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            x, y, z = map(int, line.split(','))
            points.append((x, y, z))
        n = len(points)
        edges = []
    # euclidean
        parent = list(i for i in range(n))
        size = [1]*n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            parent[rb] = ra
            size[ra] += size[rb]

        def distance(x1, y1, z1, x2, y2, z2):
            return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

        for i, j in combinations(range(n), 2):
            d = distance(*points[i], *points[j])
            edges.append((d, i, j))
        edges.sort()

        for _, i, j in edges[:1000]:
            union(i, j)
        root_sizes = [size[i] for i in range(n) if find(i) == i]
        root_sizes.sort(reverse=True)
        print(reduce(operator.mul, root_sizes[:3]))
        
def part2():
    points = []
    with open('day8/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            x, y, z = map(int, line.split(','))
            points.append((x, y, z))
    n = len(points)
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True

    def distance(x1, y1, z1, x2, y2, z2):
        return (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2

    edges = []
    for i, j in combinations(range(n), 2):
        d = distance(*points[i], *points[j])
        edges.append((d, i, j))
    edges.sort()

    li, lj = -1, -1
    for _, i, j in edges:
        if union(i, j):
            li, lj = i, j

    print(points[li][0] * points[lj][0])


part1()
part2()
