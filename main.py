#
#   Program: Row Reduction Project
#
#   Description: Simple row reduction formula project intended for MATH313 at the University of Arizona
#
#   IDE: Microsoft Visual Studios 16.8.3
#
#   Date: 2nd of September 2023
#
#   Author: Quynn Bell
#

import numpy as np

def row_reduction(matrix):
    """
    This function performs row reduction on a given matrix to convert it to row-echelon form.

    Args:
        matrix (numpy.ndarray): The input matrix as a NumPy array.

    Returns:
        matrix (numpy.ndarray): The row-echelon form of the input matrix.
    """

    # Convert the matrix to floating-point integers
    matrix = matrix.astype(float)
    # use shape to get rows and columns of the matrix
    m, n = matrix.shape
    r = 0  # Row index
    for c in range(n):
        # Find the pivot element
        pivot_row = r
        while pivot_row < m and matrix[pivot_row, c] == 0:
            pivot_row += 1

        if pivot_row == m:
            # No pivot element found in this column, move to the next column
            continue

        # Swap rows to make the pivot element the leading 1
        matrix[[r, pivot_row]] = matrix[[pivot_row, r]]

        # Scale the row to make the pivot element equal to 1
        matrix[r, :] /= matrix[r, c]

        # Eliminate other entries in the current column
        for i in range(m):
            if i != r:
                matrix[i, :] -= matrix[i, c] * matrix[r, :]

        r += 1

    threshold = 1e-10
    matrix[np.abs(matrix) < threshold] = 0

    return matrix


def test_case():
    # Define test case array
    A = np.array([[12, -7, 11, -9, 5],
              [-9, 4, -8, 7, -6],
              [-6, 11, -7, 3, -9],
              [4, -6, 10, -5, 12]])
    
    # Pass array into row_reduction function
    row_echelon_form = row_reduction(A)

    # Display output in terminal
    print("Row-Echelon Form:")
    print(row_echelon_form)


if __name__ == '__main__':
    test_case()
