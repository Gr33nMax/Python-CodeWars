"""
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9,
so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks)
contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
and returns true if it is a valid solution, or false otherwise.
The cells of the sudoku board may also contain 0's, which will represent empty cells.
Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Examples
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
"""


def valid_solution(board) -> bool:
    is_valid_solution = True
    if not board or len(board) != 9:
        is_valid_solution = False
    squares = [[] for _ in board]
    line_idx = 0
    # form squares
    for idx, line in enumerate(board, 1):
        # check each line
        if len(set(line)) != 9:
            is_valid_solution = False
        squares[line_idx].append(line[:3])
        squares[line_idx + 1].append(line[3:6])
        squares[line_idx + 2].append(line[6:])
        if idx % 3 == 0:
            line_idx += 3
    # check each square
    for square in squares:
        for sub_line in square:
            if not all(sub_line):
                is_valid_solution = False
        lists_extension = set(square[0] + square[1] + square[2])
        if len(lists_extension) != 9:
            is_valid_solution = False

    columns = list()
    # check each column
    for i in range(len(board)):
        sub_column = list()
        for j in range(len(board[i])):
            sub_column.append(board[j][i])
        if len(set(sub_column)) != 9:
            is_valid_solution = False
        columns.append(sub_column)
    return is_valid_solution


print(valid_solution([
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 3, 5]]))


"""
Other Solutions

1.
def validSolution(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)

2.
def validSolution(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows

def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not check_one_to_nine(nums):
                return False
    return True

def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True
    
def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True
            

def check_one_to_nine(lst):
    check = range(1,10)
    return sorted(lst) == check
    
3.
import numpy as np
from itertools import chain

nums = set(range(1, 10))

def validSolution(board):
    a = np.array(board)
    r = range(0, 9, 3)
    return all(set(v.flatten()) == nums for v in chain(a, a.T, (a[i:i+3, j:j+3] for i in r for j in r)))
    
4.
def validSolution(board):
    for x in range(9):
        arr = [board[y][x] for y in range(9)]
        arr2 = [board[x][y] for y in range(9)]
        arr3 = [board[i][y] for y in range(((x%3)*3),(((x%3)*3)+3)) for i in range((int(x/3)*3),(int(x/3)*3)+3)]
        for i in range(9):
            if arr[i] in arr[(i+1):]: return False
            if arr2[i] in arr2[(i+1):]: return False
            if arr3[i] in arr3[(i+1):]: return False
    return True
"""