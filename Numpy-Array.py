import numpy as np

class matrix: 

    # This functions creates matrix
    def __init__(self):
        self.array1 = np.empty # Create an array with 0 rows and 0 columns
        self.rows = int(input("How many rows is the matrix? ")) 
        self.columns = int(input("How many columns is the matrix? "))
    
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

    def row_swap(matrix):
        I_row = (int(input("Original Row? ")) - 1)
        A_row = (int(input("Row to swap? ")) - 1)
        matrix[[I_row, A_row]] = matrix [[A_row, I_row]]
        return matrix 

    
def start():
    Imatrix = matrix()
    Imatrix = Imatrix.reshape_and_fill()
    print(Imatrix)
    print(matrix.row_swap(Imatrix))

start()