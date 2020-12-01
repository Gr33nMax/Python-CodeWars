"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 when there is no smaller number that contains the same digits.
Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""


def next_smaller(n):
    # check one-digit numbers
    if n // 10 == 0:
        return -1
    str_n = str(n)
    sorted_n = sorted(str_n)
    # check the smallest numbers
    if str().join(sorted_n) == str_n:
        return -1

    # starting from the right and find the first digit that has at least one smaller digit to its right (Call it X)
    x = 0
    x_idx = 0
    prev_digit = str_n[-1]  # last digit
    for i, curr_digit in enumerate(reversed(str_n[:-1])):
        if curr_digit > prev_digit:
            x = curr_digit
            x_idx = len(str_n) - i - 2
            break
        prev_digit = curr_digit

    new_str = list(str_n)
    # find the largest digit that is to the right of X, and is smaller than X (Call it Y)
    right_to_x_rev = str_n[:x_idx:-1]
    max_num_right_to_x = max(right_to_x_rev, key=lambda t: t < x)
    y_idx = len(str_n) - right_to_x_rev.index(max_num_right_to_x) - 1
    new_str[x_idx], new_str[y_idx] = new_str[y_idx], new_str[x_idx]
    result = ''.join(new_str[:x_idx + 1]) + ''.join(sorted(new_str[x_idx + 1:], reverse=True))
    if result.startswith('0'):
        return -1
    return int(result)


# negative test cases
print(next_smaller(9))  # -1 (one digit, already smallest)
print(next_smaller(135))  # -1 (already smallest)
print(next_smaller(1027))  # -1 (leading 0)
print(next_smaller(21))
print(next_smaller(531))
print(next_smaller(2071))
print(next_smaller(1262347))
print(next_smaller(907))
print(next_smaller(135))
print(next_smaller(414))
print(next_smaller(123456798))
print(next_smaller(123456789))
print(next_smaller(1234567908))
