"""
Your goal in this kata is to implement a difference function, which subtracts one
list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a: list, b: list) -> list:
    for value in b:
        for _ in range(a.count(value)):
            a.remove(value)
    return a


print(array_diff([1, 2, 2, 2, 3, 4], [2, 4]))

"""
Other solutions
1.
def array_diff(a, b):
    return [x for x in a if x not in b]
    
2.
def array_diff(a, b):
    return filter(lambda i: i not in b, a)
"""
