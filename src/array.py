import numpy as np
from collections import deque
from typing import Deque

class Matrix: 
    def __init__(self,rows,columns) -> None:
        self.wArray = np.empty # Create an array with 0 rows and 0 columns
        self.addition_buffer_row_column = np.empty # Used to store multiplicated rows or columns, and then added
        self.subtraction_buffer_row_column = np.empty # Used to store multiplicated rows or columns, and then subtracted
        self.rows = rows 
        self.columns = columns 

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
        # Takes Input of "1 2 3"(note the spaces,  this is funcinput), uses map(func, funcinput) to apply int() to funcinput
        # Funcinput is split with " " as the separator and tuns funcinput to ['1', '2', '3']
        list_of_values = list(map(int, input('Input Matrix values, Ex: "1 2 3"\n').split()))
        if len(list_of_values) == (self.rows * self.columns):
            self.wArray = np.array(list_of_values).reshape(self.rows,self.columns)
            return self.wArray
        else:
            print("Too much or too little terms!")
            return self.reshape_and_fill() # Loops function if # of terms doesnt match what should be there

    def getArray(self) -> np.ndarray:
        """
        getter for the array object
        """
        return self.wArray

    def row_swap(self) -> np.ndarray:
        """
        swaps two rows and returns the new np.ndarray object

        Returns:
            the modified np.ndarray object
        """
        I_row = (int(input("Original Row? ")) - 1)
        A_row = (int(input("Row to swap? ")) - 1)
        self.wArray[[I_row, A_row]] = self.wArray[[A_row, I_row]]
        return self.wArray

    def col_swap(self) -> np.ndarray: 
        """
        swaps two cols and returns the new np.ndarray object

        Returns:
            the modified np.ndarray object
        """
        I_column = (int(input("Original column? ")) - 1)
        A_column = (int(input("column to swap? ")) - 1)
        self.wArray[:, [I_column, A_column]] = self.wArray[:, [A_column, I_column]]
        return self.wArray

    def multiply_row(self) -> np.ndarray:
        """
        multiplies a chosen row with a scalar

        Returns:
            the modified np.ndarray object
        """
        row = (int(input("Which Row? ")) - 1)
        multiple = (int(input("What Number? ")))
        self.wArray[row, :] = np.multiply(self.wArray[row, :],multiple) # Yes, you couse use *, but I like this for readablity
        return self.wArray

    def multiply_column(self) -> np.ndarray:
        """
        multiplies the chosen column with a scalar

        Returns:
            the modified np.ndarray object
        """
        column = (int(input("Which column? ")) - 1)
        multiple = (int(input("What Number? ")))
        self.wArray[:, column] = np.multiply(self.wArray[:, column],multiple) # ":" means select all rows or columns depending on where it is placed
        return self.wArray
    
    def row_addition(self) -> np.ndarray: # Might need subarrays, numpy doesnt seem to provide a way to add values within the same matrix
        """
        adds one row to another

        Returns:
            the modified np.ndarray object
        """
        I_row = (int(input("Row to be added to? ")) - 1)
        A_row = (int(input("Row added to other row? ")) - 1)
        A_row_multiple = int(input("What is 2nd row multplied by? "))
        self.addition_buffer_row_column = np.multiply(self.wArray[A_row, :], A_row_multiple)
        self.wArray[I_row, :] = np.array([term1 + term2 for term1, term2 in zip(self.wArray[I_row, :], self.addition_buffer_row_column)])
        self.addition_buffer_row_column = np.empty
        return self.wArray
    
    def col_addition(self) -> np.ndarray:
        """
        adds one column to another

        Returns:
            the modified np.ndarray object
        """
        I_col = (int(input("column to be added to? ")) - 1)
        A_col = (int(input("column added to other column? ")) - 1)
        A_col_multiple = int(input("What is 2nd column multplied by? "))
        self.addition_buffer_row_column = np.multiply(self.wArray[:, A_col], A_col_multiple)
        self.wArray[:, I_col] = np.array([term1 + term2 for term1, term2 in zip(self.wArray[:, I_col], self.addition_buffer_row_column)])
        self.addition_buffer_row_column = np.empty
        return self.wArray

    def row_subtraction(self) -> np.ndarray:
        """
        subtracts one row from another

        Returns:
            the modified np.ndarray object
        """
        I_row = (int(input("Row to be subtracted from? ")) - 1)
        A_row = (int(input("Row used to subtract? ")) - 1)
        A_row_multiple = int(input("What is 2nd row multplied by? "))
        self.subtraction_buffer_row_column = np.multiply(self.wArray[A_row, :], A_row_multiple)
        self.wArray[I_row, :] = np.array([term1 - term2 for term1, term2 in zip(self.wArray[I_row, :], self.subtraction_buffer_row_column)])
        self.subtraction_buffer_row_column = np.empty
        return self.wArray
    
    def col_subtraction(self) -> np.ndarray: 
        """
        subtracts one column from another

        Returns:
            the modified np.ndarray object
        """
        I_col = (int(input("column to be subtracted from? ")) - 1)
        A_col = (int(input("column used to subtract? ")) - 1)
        A_col_multiple = int(input("What is 2nd col multplied by? "))
        self.subtraction_buffer_row_column = np.multiply(self.wArray[:, A_col], A_col_multiple)
        self.wArray[:, I_col] = np.array([term1 - term2 for term1, term2 in zip(self.wArray[:, I_col], self.subtraction_buffer_row_column)])
        self.subtraction_buffer_row_column = np.empty
        return self.wArray
    
    def deter_finder(self) -> float:
        """
        Finds the determinant of the given np.ndarray object

        returns:
            the determinant, as a float
        """
        return int(np.linalg.det(self.wArray))
    
    def transpose(self) -> np.ndarray:
        """
        transposes the matrix 

        returns:
            a view of the modified np.ndarray
        """
        self.wArray = np.transpose(self.wArray)
        return self.wArray
    
    # TODO: Add adjoint of a matrix
    
    # def inv_finder(): # Will give floats, not sure how to solve

    def __str__(self) -> None:
        """
        prints a string representation of the ndarray object
        """
        print(np.array2string(self.wArray))
        # printString = "["
        # nums = self.wArray.shape
        # rows = nums[0]
        # cols = nums[1]
        # for i in range(rows):
        #     printString = printString + "\n"
        #     for j in range(cols):
        #         printString = printString + str(self.wArray[i][j]) + " "
        # printString = printString + "\n]"
        # print(printString)


# Used for creating and using the matrix deques.
class MatrixStorage:
    """
    Used to store previous iterations of the matrix
    """
    def __init__(self, input_matrix: Matrix | None):
        self.matrixDeque : Deque[np.ndarray] = deque()        
        if input_matrix is not None:
            self.matrixDeque.append(input_matrix.getArray())

    def restorePrevMatrix(self) -> np.ndarray:
        """
        restores the previous iteration of the array object

        returns:
            a np.ndarray object

        raises:
            IndexError if the deque is currently empty
        """
        if len(self.matrixDeque) > 0:
            return self.matrixDeque.pop()
        else:
            raise IndexError
    
    def addMatrix(self, matrix: Matrix | None) -> None:
        """
        adds a iteration of an ndarray into the deque
        """
        if matrix is not None:
            self.matrixDeque.append(np.copy(matrix.getArray()))
        else:
            raise ValueError("matrix not found!")