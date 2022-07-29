import numpy as np

class matrix: 

    # This functions creates matrix
    def __init__(self):

        # Create an array with 0 rows and 0 columns
        self.array1 = np.empty
        rows = int(input("How many rows is the matrix? ")) 
        columns = int(input("How many columns is the matrix? "))

        # Takes Input of "1 2 3"(note the spaces,  this is funcinput), uses map(func, funcinput) to apply int() to funcinput
        # Funcinput is split with " " as the separator and tuns funcinput to ['1', '2', '3']
        list_of_values = list(map(int, input('Input Matrix values, Ex: "1 2 3" ').split()))
        self.array1 = np.array(list_of_values).reshape(rows,columns)

    # Throws Error, might need to be moved out of class
    def display_matrix(self):
        print(array1) # Naturally fomatted with rows and columns due to numpy

    # Needs more work for all functions below comment
    def row_swap(self):
        I_row = int(input("Original Row? "))
        A_row = int(input("Row to swap? "))
        


