"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
from collections import Counter


def find_it(seq: list) -> int:
    return list(filter(lambda x: x[1] % 2 == 1, Counter(seq).items()))[0][0]


"""
Other Solutions

1.
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

2.
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
    
3.
from collections import Counter
def find_it(l):
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]
    
4.
def find_it(seq):
    result = 0
    for x in seq:
        result ^= x
    return result
"""
