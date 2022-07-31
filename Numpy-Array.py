import numpy as np

class matrix: 
    # This functions creates matrix
    def __init__(self,rows,columns):
        self.array1 = np.empty # Create an array with 0 rows and 0 columns
        self.rows = rows 
        self.columns = columns 
  
    # This Functions does as named
    def reshape_and_fill(self): 
        # Takes Input of "1 2 3"(note the spaces,  this is funcinput), uses map(func, funcinput) to apply int() to funcinput
        # Funcinput is split with " " as the separator and tuns funcinput to ['1', '2', '3']
        list_of_values = list(map(int, input('Input Matrix values, Ex: "1 2 3"\n ').split()))
        if len(list_of_values) == (self.rows * self.columns):
            self.array1 = np.array(list_of_values).reshape(self.rows,self.columns)
            return self.array1
        else:
            print("Too much or too little terms!")
            return self.reshape_and_fill() # Loops function if # of terms doesnt match what should be there

    def rowcol_swap(self):
        I_row = (int(input("Original Row? ")) - 1)
        A_row = (int(input("Row to swap? ")) - 1)
        self.array1[[I_row, A_row]] = self.array1[[A_row, I_row]]
        return self.array1
    
    def col_swap(self): 
        I_column = (int(input("Original column? ")) - 1)
        A_column = (int(input("column to swap? ")) - 1)
        self.array1[:, [I_column, A_column]] = self.array1[:, [A_column, I_column]]
        return self.array1

    def multiply_row(self):
        row = (int(input("Which Row? ")) - 1)
        multiple = (int(input("What Number? ")))
        self.array1[row, :] = np.multiply(self.array1[row, :],multiple) # Yes, you couse use *, but I like this for readablity
        return self.array1

    def multiply_column(self):
        column = (int(input("Which column? ")) - 1)
        multiple = (int(input("What Number? ")))
        self.array1[:, column] = np.multiply(self.array1[:, column],multiple) # ":" means select all rows or columns
        return self.array1
    
    def row_addition(self): # Might need subarrays, numpy doesnt seem to provide a way to add values within the same matrix
        I_row = (int(input("Row to be added to? ")) - 1)
        A_row = (int(input("Row added to other row? ")) - 1)
        A_row_multiple = int(input("What is 2nd row multplied by? "))


def start():
    rows = int(input("How many rows? "))
    columns = int(input("How many Columns? "))
    Matrix_Use = matrix(rows, columns)
    Matrix_Use.reshape_and_fill()
    print(Matrix_Use.multiply_column())

start()