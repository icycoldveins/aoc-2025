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


import sys
from collections import Counter


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
                    if fn(num):
                        cnt += num
    return cnt



'''
--- Day 2: Gift Shop ---
--- Part Two ---
The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules?
'''


def solve2():
    def fn(s):
        s = str(s)
        bounds = len(s)//2
        for r in range(1, bounds+1):
            sub = s[:r]
            times = len(s)//len(sub)
            if sub * times == s:
                return True
        return False

    cnt = 0
    with open('day2/input.txt', 'r') as f:
        for line in f:
            for ranges in line.split(','):
                start, end = map(int, ranges.split('-'))
                for num in range(start, end+1):
                    if fn(num):
                        cnt += num
    return cnt
print(solve2())