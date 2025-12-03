'''
pwd changed 

dials 0 through 99 

click as it reaches each num 

L, R which dir to go
rotation has distance value 
how many clicks dial gotta go that way 

clock and anti clock 

how many times it is 0 when you rotate

start at 50 
'''


def solve():
    pos = 50
    cnt = 0
    mem = {
        'L': -1,
        'R': 1
    }
    with open('day1/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            d = mem[line[:1]]
            m = int(line[1:])
            pos += (d*m)
            pos %= 100
            if not pos:
                cnt += 1
    return cnt
def solve2():
    pos = 50
    cnt = 0
    mem = {
        'L': -1,
        'R': 1
    }
    with open('day1/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            d = mem[line[:1]]
            m = int(line[1:])
            pos += (d*m)
            pos %= 100
            if not pos:
                cnt += 1
    return cnt