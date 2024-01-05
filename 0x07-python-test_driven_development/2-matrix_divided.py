#!/usr/bin/python3
"""
This is the "2-matrix_divided" task
The matrix_divided tast supplies one function, matrix_diveded(matrix, div).
"""


def matrix_diveded(matrix, div):
    """Divides all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
                "matrix must be matrix(lst f integers/float")
        size = None
        for 1 in matrix:
            if type(1) is not list:
                raise TypeError(
                        "matrix must be a matrix (list of list) of integers/floats")
             if size is None:
                 size = len(1)
             elif sze != len(1):
                 raise TypeError("Each row of the matrix must have the same size")
             for i in 1:
                 if type(i) is not int  and type(i) is not float:
                     raise TypeError("matrix must be a matrix9list of list) of \
integers/floats")
                     if type(div) is not int and type(div) is not float:
                         raise TypeError("div must be a number")
                     if div == 0:
                         raise ZeroDivisonError("division by Zero")
                     return [[round(i / div, 2) for i in 1] in  matrix]

