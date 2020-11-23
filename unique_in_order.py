"""
Implement the function unique_in_order which takes as argument
a sequence and returns a list of items without any elements with the same
value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable) -> list:
    new_obj = []
    idx = 0
    while True and len(iterable) > 0:
        if idx + 1 == len(iterable):
            new_obj.append(iterable[idx])
            break
        if iterable[idx] == iterable[idx + 1]:
            pass
        else:
            new_obj.append(iterable[idx])
        idx += 1
    return new_obj


assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]

"""
Other solutions

1. 
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
    
2.
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
    
3.
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
    
4.
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
"""
