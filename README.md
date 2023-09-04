# Row Reduction Project

## Description
This is a simple row reduction formula project intended for MATH313 at the University of Arizona. It allows you to perform row reduction on a given matrix to convert it to row-echelon form. The code is implemented in Python and uses the NumPy library.

## Prerequisites
- Python 3
- NumPy library

## Usage
1. Make sure you have Python 3 and the NumPy library installed.
2. Clone or download this repository to your local machine.
3. Open the code in an integrated development environment (IDE) that supports Python, such as Microsoft Visual Studio.
4. Run the code, and it will prompt you to enter the number of rows and columns for your matrix. Then, you can input the matrix elements row-wise.
5. The code will display the initial matrix and its row-echelon form in the terminal.

## Author
Quynn Bell

## Functions
### 'row_reduction(matrix)'
This function performs row reduction on a given matrix to convert it to row-echelon form.

Args:
    matrix (numpy.ndarray): The input matrix as a NumPy array.

Returns:
    matrix (numpy.ndarray): The row-echelon form of the input matrix.

### 'input_matrix()'
Prompt the user for the number of rows and columns of a matrix, and then collect the matrix elements.

Returns:
    numpy.ndarray: The matrix entered by the user.

### 'test_case(matrix=np.array)'
This function is used to test the row reduction functionality with an optional input matrix. If no matrix is provided, a default test case will be used.

Args:
    matrix (numpy.ndarray, optional): The input matrix for testing.

### NOTE
This code is still a work in progress and may provide incorrect answers.