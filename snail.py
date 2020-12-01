"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements
to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""


def snail(snail_map):
    if not snail_map[0]:
        return []
    result_lst = list()
    direction = 'right'
    done = False
    imin = 0
    jmin = 0
    imax = len(snail_map) - 1
    jmax = imax
    while not done:
        if direction == 'right':
            i = imin
            for j in range(jmin, jmax + 1):
                result_lst.append(snail_map[i][j])
            direction = 'down'
            imin += 1
        elif direction == 'down':
            j = jmax
            for i in range(imin, imax + 1):
                result_lst.append(snail_map[i][j])
            direction = 'left'
            jmax -= 1
        elif direction == 'left':
            i = imax
            for j in range(jmax, jmin - 1, -1):
                result_lst.append(snail_map[i][j])
                direction = 'up'
            imax -= 1
        elif direction == 'up':
            j = jmin
            for i in range(imax, imin - 1, -1):
                result_lst.append(snail_map[i][j])
            direction = 'right'
            jmin += 1

        if imin > imax or jmin > jmax:
            done = True
    return result_lst


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

array2 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

array3 = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

array4 = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]

print(snail(array3))
print(snail([[]]))


"""
Other Solutions

1.
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret

2.
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out
    
3.
def snail(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []
"""