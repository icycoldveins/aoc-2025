'''
eight adjacent positions 
so diags and nswe directions? 

brute force iteration and check all 8 directoins
'''


def part1():
    grid = []
    with open('day4/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))
    row = len(grid)
    col = len(grid[0])
    directions = (
        [1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]
    )

    def bounds(x, y):
        return 0 <= x < row and 0 <= y < col

    def validate(x, y):
        cnt = 0
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if bounds(nx, ny) and grid[nx][ny] == '@':
                cnt += 1
        return cnt < 4

    cnt = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] in '@' and validate(i, j):
                cnt += 1
    return cnt


def part2():
    grid = []
    with open('day4/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))
    row = len(grid)
    col = len(grid[0])
    directions = (
        [1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]
    )

    def bounds(x, y):
        return 0 <= x < row and 0 <= y < col

    def validate(x, y):
        cnt = 0
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if bounds(nx, ny) and grid[nx][ny] == '@':
                cnt += 1
        return cnt < 4

    # if we can take then we could make more rolls less rolls = more options stop if we cant take any at all
    cnt = 0
    possible = True
    while possible:
        possible = False
        for i in range(row):
            for j in range(col):
                if grid[i][j] in '@' and validate(i, j):
                    grid[i][j] = '.'
                    cnt += 1
                    possible = True
    return cnt


print(part2())
