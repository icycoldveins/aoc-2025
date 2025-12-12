def parse_input(filename):
    """Parse shapes and regions from input file."""
    with open(filename) as f:
        content = f.read()

    lines = content.strip().split('\n')
    current_shape = []
    shapes = []

    for line in lines:
        if ':' in line and 'x' not in line:
            if current_shape:
                shapes.append(parse_shape(current_shape))
            current_shape = []
        elif 'x' in line and ':' in line:
            if current_shape:
                shapes.append(parse_shape(current_shape))
            break
        elif line.strip() and not line[0].isdigit():
            current_shape.append(line)

    regions = []
    for line in lines:
        if 'x' in line and ':' in line:
            regions.append(parse_region(line))

    return shapes, regions


def parse_shape(rows):
    """Convert shape rows to set of (row, col) coordinates."""
    cells = set()
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == '#':
                cells.add((r, c))
    return cells


def parse_region(line):
    """Parse region line like '12x5: 1 0 1 0 3 2'."""
    dims, counts = line.split(': ')
    width, height = map(int, dims.split('x'))
    shape_counts = list(map(int, counts.split()))
    return width, height, shape_counts


def part1():
    shapes, regions = parse_input('day12/input.txt')
    shape_sizes = [len(s) for s in shapes]

    count = 0
    for width, height, shape_counts in regions:
        grid_area = width * height
        total_needed = sum(shape_sizes[i] * c for i, c in enumerate(shape_counts))
        if total_needed <= grid_area:
            count += 1

    print(f"Part 1: {count}")
    return count


if __name__ == '__main__':
    part1()
