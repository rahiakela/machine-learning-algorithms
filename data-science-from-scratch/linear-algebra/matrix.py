"""
A matrix is a two-dimensional collection of numbers. We will represent matrices as lists of lists,
with each inner list having the same size and representing a row of the matrix. If A is a matrix,
then A[i][j] is the element in the ith row and the jth column.
"""
from typing import List
from typing import Tuple


Matrix = List[List[float]]

# A has 2 rows and 3 columns
A = [
    [1, 2, 3],
    [4, 5, 6]
]
# B has 3 rows and 2 columns
B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# the matrix A has len(A) rows and len(A[0]) columns, which we consider its shape
def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # number of elements in first row
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns
