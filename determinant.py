#
#   Program: Row Reduction Project
#
#   Description: Simple determinant formula project intended for MATH313 at the University of Arizona
#
#   IDE: Microsoft Visual Studios 16.8.3
#
#   Date: 6th of November 2023
#
#   Author: Quynn Bell
#

import numpy as np
import copy

def determinant(matrix: np.array):
    # Converting matrix into floating-point integers
    matrix = np.array(matrix, dtype=float)

    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square to calculate its determinant")

    # Determine the size of the matrix
    n = matrix.shape[0]
    
    # Base case: If the matrix is 1x1, return its only element as the determinant
    if n == 1:
        return matrix[0, 0]

    # Initialize the determinant variable
    det = 0

    # Loop through the first row of the matrix to calculate the determinant
    for j in range(n):
        # Calculate the cofactor of the element at the 0th row and j-th column
        submatrix = np.delete(matrix, 0, 0)
        submatrix = np.delete(submatrix, j, 1)

        # Recursively calculate the determinant of the submatrix
        cofactor = matrix[0, j] * determinant(submatrix)
        
        # Add or subtract the cofactor based on the column index (j)
        det += (-1) ** j * cofactor

    return det


def input_matrix():
    """
    Prompt the user for the number of rows and columns of a matrix, and then collect the matrix elements.

    Returns:
        numpy.ndarray: The matrix entered by the user.
    """
    try:
        
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



def test_case():
    #To make random matrices, initialize the built-in random number generator as rng
    rng = np.random.default_rng()

    #Make 10 random 3 x 3 matrices, and test whether or not your program computes the determinant correctly
    for i in range(50):
        m=rng.integers(-3,3,size=(3,3))
        mcopy=copy.deepcopy(m)

        # remember that our program modifies its input, so we need to save a copy that will remain unmodified
        correct_det = np.linalg.det(m)
        our_det = determinant(m)

        rounded_custom = round(our_det, 10)
        rounded_numpy = round(correct_det, 10)

        print(rounded_custom, rounded_numpy)
        #To test whether or not your program output is in echelon form, convert the array to type Matrix from sympy library, and check attribute is_echelon
        if (our_det == correct_det) == False:
            print(mcopy,correct_det,our_det)


def run():
    # Prompt the user for a second matrix
    print("\nEnter the first matrix:")
    user_matrix = input_matrix()
    
    # Prompt the user for a second matrix
    print("\nEnter the second matrix:")
    user_matrix2 = input_matrix()

    # Calculate the determinants
    det_A = determinant(user_matrix)
    det_B = determinant(user_matrix2)
    det_sum = determinant(user_matrix + user_matrix2)

    # Compare the results
    print(f"det(A + B): {det_sum}")
    print(f"det(A) + det(B): {det_A + det_B}")



if __name__ == '__main__':
    test_case()
    """
    print('This is a simple determinant program. Please enter the following information:')
    run()
    """