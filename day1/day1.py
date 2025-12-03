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
'''
now we somehow need to know when we make a rotation one way or not

if we go left we pass 0 how can we capture passing 0 
if we have a negative number or 0
then what if we do that muiltiple times

if we got right if we pass 0 

if we get distance traveled going left or right after iterations 
    if I know how much I travelled going so if I go left the distance has to be 
    - 40 because we lost that much distance
    + 40 if go right because we have extra distnce
'''
def solve2():
    pos = 50
    cnt = 0
    mem = {
        'L': -1,
        'R': 1
    }
    def helper(pos, delta, right):
        if not pos:
            return delta // 100
        if right:
            return (pos + delta) // 100
        if delta < pos:
            return 0
        return (delta - pos) // 100 + 1

    with open('day1/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            d = mem[line[:1]]
            m = int(line[1:])
            cnt += helper(pos, m, False if d < 0 else True)
            pos += (d * m)
            pos %= 100
    return cnt
print(solve2())