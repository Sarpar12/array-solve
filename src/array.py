"""
contains the classes and functionality used in main.py
"""
from collections import deque
from typing import Deque, List
import numpy as np
from dataclasses import dataclass

class Matrix:
    """
    the matrix class, acts as a wrapper around a np.ndarray object
    """
    def __init__(self,rows: int,columns: int, float_list: List[float] | None) -> None:
        """
        creates a Matrix object. If a initial list is not provided, then 
        the user will be asked for input.

        `params:`
            rows {int}: the amount of rows in the matrix
            columns {int}: the amount of columns in the matrix
            float_list {list[float]}: the initialization list, optional
        """
        self.addition_buffer_row_column = np.empty
        self.subtraction_buffer_row_column = np.empty 
        self.rows = rows
        self.columns = columns
        if float_list is not None:
            self.matrix_array = np.array(float_list).reshape(rows, columns)
        else:
            self.matrix_array = np.empty
            self.reshape_and_fill()

    # This Functions does as named
    def reshape_and_fill(self) -> None: 
        """
        Takes an input and converts into an np.ndarray with the right dimensions

        For example, if the given dimensions were 2x2, and the input was "1 2 3 4",
        the resulting array would look like:

        [
          1  2 

          3  4
        ]
        """
        # Funcinput is split with " " as the separator and tuns funcinput to ['1', '2', '3']
        list_of_values = list(map(float, input('Input Matrix values, Ex: "1 2 3"\n').split()))
        if len(list_of_values) == (self.rows * self.columns):
            self.matrix_array = np.array(list_of_values).reshape(self.rows,self.columns)
            return self.matrix_array
        else:
            print("Too much or too little terms!")
            return self.reshape_and_fill() # Loops function if # of terms doesnt match

    def get_array(self) -> np.ndarray:
        """
        getter for the array object
        """
        return self.matrix_array

    def row_swap(self) -> np.ndarray:
        """
        swaps two rows and returns the new np.ndarray object

        Returns:
            the modified np.ndarray object
        """
        i_row = int(input("Original Row? ")) - 1
        a_row = int(input("Row to swap? ")) - 1
        self.matrix_array[[i_row, a_row]] = self.matrix_array[[a_row, i_row]]
        return self.matrix_array

    def col_swap(self) -> np.ndarray: 
        """
        swaps two cols and returns the new np.ndarray object

        Returns:
            the modified np.ndarray object
        """
        i_column = int(input("Original column? ")) - 1
        a_column = int(input("column to swap? ")) - 1
        self.matrix_array[:, [i_column, a_column]] = self.matrix_array[:, [a_column, i_column]]
        return self.matrix_array

    def multiply_row(self) -> np.ndarray:
        """
        multiplies a chosen row with a scalar

        Returns:
            the modified np.ndarray object
        """
        row = int(input("Which Row? ")) - 1
        multiple = int(input("What Number? "))
        self.matrix_array[row, :] = np.multiply(self.matrix_array[row, :],multiple)
        return self.matrix_array

    def multiply_column(self) -> np.ndarray:
        """
        multiplies the chosen column with a scalar

        Returns:
            the modified np.ndarray object
        """
        column = int(input("Which column? ")) - 1
        multiple = int(input("What Number? "))
        self.matrix_array[:, column] = np.multiply(self.matrix_array[:, column],multiple) # ":" means select all rows or columns depending on where it is placed
        return self.matrix_array

    def row_addition(self) -> np.ndarray: # numpy doesnt seem to provide a way to add values within the same matrix
        """
        adds one row to another

        Returns:
            the modified np.ndarray object
        """
        i_row = int(input("Row to be added to? ")) - 1
        a_row = int(input("Row added to other row? ")) - 1
        a_row_multiple = int(input("What is 2nd row multplied by? "))
        self.addition_buffer_row_column = np.multiply(self.matrix_array[a_row, :], a_row_multiple)
        self.matrix_array[i_row, :] = np.array([term1 + term2 for term1, term2 in zip(self.matrix_array[i_row, :], self.addition_buffer_row_column)])
        self.addition_buffer_row_column = np.empty
        return self.matrix_array

    def col_addition(self) -> np.ndarray:
        """
        adds one column to another

        Returns:
            the modified np.ndarray object
        """
        i_col = int(input("column to be added to? ")) - 1
        a_col = int(input("column added to other column? ")) - 1
        a_col_multiple = int(input("What is 2nd column multplied by? "))
        self.addition_buffer_row_column = np.multiply(self.matrix_array[:, a_col], a_col_multiple)
        self.matrix_array[:, i_col] = np.array([term1 + term2 for term1, term2 in zip(self.matrix_array[:, i_col], self.addition_buffer_row_column)])
        self.addition_buffer_row_column = np.empty
        return self.matrix_array

    def row_subtraction(self) -> np.ndarray:
        """
        subtracts one row from another

        Returns:
            the modified np.ndarray object
        """
        i_row = int(input("Row to be subtracted from? ")) - 1
        a_row = int(input("Row used to subtract? ")) - 1
        a_row_multiple = int(input("What is 2nd row multplied by? "))
        self.subtraction_buffer_row_column = np.multiply(self.matrix_array[a_row, :], a_row_multiple)
        self.matrix_array[i_row, :] = np.array([term1 - term2 for term1, term2 in zip(self.matrix_array[i_row, :], self.subtraction_buffer_row_column)])
        self.subtraction_buffer_row_column = np.empty
        return self.matrix_array

    def col_subtraction(self) -> np.ndarray:
        """
        subtracts one column from another

        Returns:
            the modified np.ndarray object
        """
        i_col = int(input("column to be subtracted from? ")) - 1
        a_col = int(input("column used to subtract? ")) - 1
        a_col_multiple = int(input("What is 2nd col multplied by? "))
        self.subtraction_buffer_row_column = np.multiply(self.matrix_array[:, a_col], a_col_multiple)
        self.matrix_array[:, i_col] = np.array([term1 - term2 for term1, term2 in zip(self.matrix_array[:, i_col], self.subtraction_buffer_row_column)])
        self.subtraction_buffer_row_column = np.empty
        return self.matrix_array

    def deter_finder(self) -> float:
        """
        Finds the determinant of the given np.ndarray object

        returns:
            the determinant, as a float
        """
        return float(np.linalg.det(self.matrix_array))

    def transpose(self) -> np.ndarray:
        """
        transposes the matrix 

        returns:
            a view of the modified np.ndarray
        """
        self.matrix_array = np.transpose(self.matrix_array)
        return self.matrix_array 

    def __str__(self) -> str:
        """
        prints a string representation of the ndarray object
        """
        return np.array2string(self.matrix_array)


# Used for creating and using the matrix deques.
class MatrixStorage:
    """
    Used to store previous iterations of the matrix

    `params:`
        input_matrix {Matrix}: a Matrix object, optional
    """
    def __init__(self, input_matrix: Matrix | None = None):
        self.matrix_deque : Deque[np.ndarray] = deque()
        if input_matrix is not None:
            self.matrix_deque.append(input_matrix.get_array())

    def restore_prev_matrix(self) -> np.ndarray:
        """
        restores the previous iteration of the array object

        returns:
            a np.ndarray object

        raises:
            IndexError if the deque is currently empty
        """
        if len(self.matrix_deque) > 0:
            return self.matrix_deque.pop()
        else:
            raise IndexError

    def add_matrix(self, matrix: Matrix | None = None) -> None:
        """
        adds a copy of an iteration of an ndarray into the deque

        `params:`
            matrix {Matrix}: a instance of the Matrix class
        """
        if matrix is not None:
            self.matrix_deque.append(np.copy(matrix.get_array()))
        else:
            raise ValueError("matrix not found!")

@dataclass
class MatrixWrapper():
    """
    dataclass used to store a matrix and it's corresponding matrixStorage class
    """
    def __init__(self, matrix : Matrix, stack : MatrixStorage):
        self.matrix = matrix
        self.stack = stack
    
    def __str__(self):
        """
        prints the original matrix only
        """
        return self.matrix.__str__()