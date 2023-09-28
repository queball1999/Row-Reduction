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

    steps = []  # List to store solution steps
    matrix = matrix.astype(float)   # Convert the matrix to floating-point integers
    m, n = matrix.shape # use shape to get rows and columns of the matrix
    r = 0  # Row index
    steps.append(matrix.copy()) # Add matrix to steps
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

    return matrix, steps


def input_matrix():
    """
    Prompt the user for the number of rows and columns of a matrix, and then collect the matrix elements.

    Returns:
        numpy.ndarray: The matrix entered by the user.
    """
    try:
        ascii_art()
        print('This is a simple row reduction program. Please enter the following information:')
        # Prompt the user for the number of rows and columns
        num_rows = int(input("Enter the number of rows: "))
        num_cols = int(input("Enter the number of columns: "))

        # Initialize an empty matrix
        matrix = np.zeros((num_rows, num_cols))

        # Prompt the user for each element of the matrix
        print("Enter matrix elements row-wise:")
        for i in range(num_rows):
            for j in range(num_cols):
                matrix[i, j] = float(input(f"Enter element at row {i + 1}, column {j + 1}: "))

        return matrix

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return input_matrix()


def ascii_art():
    print("""
          _____                 _____          _            _   _              
         |  __ \               |  __ \        | |          | | (_)             
         | |__) |_____      __ | |__) |___  __| |_   _  ___| |_ _  ___  _ __   
         |  _  // _ \ \ /\ / / |  _  // _ \/ _` | | | |/ __| __| |/ _ \| '_ \  
         | | \ \ (_) \ V  V /  | | \ \  __/ (_| | |_| | (__| |_| | (_) | | | | 
         |_|  \_\___/ \_/\_/   |_|  \_\___|\__,_|\__,_|\___|\__|_|\___/|_| |_|
         """, end='\n\n')

def test_case(matrix=np.array):
    """
    This function is used to test the row reduction functionality with an optional input matrix. If no matrix is provided, a default test case will be used.

    Args:
        matrix (numpy.ndarray, optional): The input matrix for testing.
    """
    # If no matrix is passed as parameter, define default test case
    if not matrix.any():
        # Define test case array
        matrix = np.array([[12, -7, 11, -9, 5],
                  [-9, 4, -8, 7, -6],
                  [-6, 11, -7, 3, -9],
                  [4, -6, 10, -5, 12]])
    
    # Pass array into row_reduction function
    row_echelon_form, steps = row_reduction(matrix)

    # Display output in terminal
    print('Here are the solution steps:')
    for i, step_matrix in enumerate(steps):
        print(f"Step {i + 1}:")
        print(step_matrix)
        print()

    print("Row-Echelon Form:")
    print(row_echelon_form)

if __name__ == '__main__':
    user_matrix = input_matrix()
    test_case(user_matrix)
