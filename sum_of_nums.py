"""
Given two integers a and b, which can be positive or negative,
find the sum of all the integers between including them too and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""
import unittest


def get_sum(a, b):
    if a == b:
        return a
    if a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))


# simple tests
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(get_sum(1, 0), 1, 'Should be 1')
        self.assertEqual(get_sum(1, 2), 3, 'Should be 3')
        self.assertEqual(get_sum(0, 1), 1, 'Should be 1')
        self.assertEqual(get_sum(1, 1), 1, 'Should be 1')
        self.assertEqual(get_sum(-1, 0), -1, 'Should be -1')
        self.assertEqual(get_sum(-1, 2), 2, 'Should be 2')


if __name__ == "__main__":
    unittest.main()

"""
Other Solutions
1.
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
2.
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
"""
