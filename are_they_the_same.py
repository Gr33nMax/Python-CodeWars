"""
Given two arrays a and b write a function comp(a, b) that checks whether the two arrays have the "same" elements,
with the same multiplicities. "Same" means, here, that the elements in b are
the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11,
14641 is the square of 121, 20736 the square of 144, 361 the square of 19,
 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] or None
If a or b are None, the problem doesn't make sense so return false.
"""
from functools import reduce
from itertools import chain


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if not array1 and not array2:
        return True
    return not bool(reduce(lambda x, y: x ^ y, chain(map(lambda x: x ** 2, array1), array2)))


a1 = [121, 144, 19, 161, 19, 144, 19, 11, 11]
a2 = [11 * 11, 11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]

print(comp(a1, a2))

"""
Other Solutions

1.
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
"""