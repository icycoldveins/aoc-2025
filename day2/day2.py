'''
so ids are separated by , and -

so a seq twice is invalid basically?
5 twice
64 twice
123 twice

basically loop through the ranges and then determine if we can derive a sequence

dp table? 
    need to extract multiple seqs like 112
just take half and compare both if rep twice , then split should be equal 

'''


def solve():
    def fn(x):
        x = str(x)
        half = len(x)//2
        return x[half:] == x[:half]
    cnt = 0
    with open('day2/input.txt', 'r') as f:
        for line in f:
            for ranges in line.split(','):
                start, end = map(int, ranges.split('-'))
                for num in range(start, end+1):
                    if fn(num): cnt += num
    return cnt
print(solve())
