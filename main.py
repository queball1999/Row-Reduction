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
from sympy import Matrix

rng = np.random.default_rng()

def row_echelon(A):
    # get the number of rows and columns of A to use in for loops
    r, c = A.shape
    # perform row reduction on matrix from second row
    for j in range(c):
        for i in range(j+1, r):
            if A[j,j] != 0.0:
                ratio = A[i,j]/A[j,j]
                A[i] = A[i] - ratio * A[j]

    return A

def test_case():
    for i in range(10**2):
        m=rng.integers(-3,3,size=(3,3))
        efm=row_echelon(m)
        #To test whether or not your program output is in echelon form, convert the array to type Matrix from sympy library, and check attribute is_echelon
        test=Matrix(efm).is_echelon
        if test == False:
                print(m)
                print(efm)

if __name__ == '__main__':
    test_case()

