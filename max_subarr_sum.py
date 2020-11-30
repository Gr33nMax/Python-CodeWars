"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous
subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""
from functools import reduce


def max_sequence(arr: list) -> int:
    # empty list or all numbers are negative
    if not arr or all(map(lambda x: x < 0, arr)):
        return 0

    def gen_sequences():
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                yield reduce(lambda a, b: a + b, arr[i:j])

    result = gen_sequences()
    return max(result)


print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))


"""
Other Solutions

1.
def maxSequence(arr):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0
        if curr > max:
            max = curr
    return max
    
2.
def maxSequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans

3.
def maxSequence(arr):
    return max(maxSequence(arr[1:]), max(reduce(lambda sums, n: sums + [sums[-1]+n], arr, [0]))) if arr else 0

4.
from itertools import accumulate
def maxSequence(arr):
    return max(accumulate(arr + [0], lambda a, b: max(a + b, 0)))
"""
