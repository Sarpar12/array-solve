import numpy as np

class matrix: 
    # This functions creates matrix
    def __init__(self,rows,columns):
        self.wArray = np.empty # Create an array with 0 rows and 0 columns
        self.addition_buffer_row_column = np.empty # Used to store multiplicated rows or columns, and then added
        self.subtraction_buffer_row_column = np.empty # Used to store multiplicated rows or columns, and then subtracted
        self.rows = rows 
        self.columns = columns 

  
    # This Functions does as named
    def reshape_and_fill(self): 
        # Takes Input of "1 2 3"(note the spaces,  this is funcinput), uses map(func, funcinput) to apply int() to funcinput
        # Funcinput is split with " " as the separator and tuns funcinput to ['1', '2', '3']
        list_of_values = list(map(int, input('Input Matrix values, Ex: "1 2 3"\n').split()))
        if len(list_of_values) == (self.rows * self.columns):
            self.wArray = np.array(list_of_values).reshape(self.rows,self.columns)
            return self.wArray
        else:
            print("Too much or too little terms!")
            return self.reshape_and_fill() # Loops function if # of terms doesnt match what should be there

    def row_swap(self):
        I_row = (int(input("Original Row? ")) - 1)
        A_row = (int(input("Row to swap? ")) - 1)
        self.wArray[[I_row, A_row]] = self.wArray[[A_row, I_row]]
        return self.wArray
    
    def col_swap(self): 
        I_column = (int(input("Original column? ")) - 1)
        A_column = (int(input("column to swap? ")) - 1)
        self.wArray[:, [I_column, A_column]] = self.wArray[:, [A_column, I_column]]
        return self.wArray

    def multiply_row(self):
        row = (int(input("Which Row? ")) - 1)
        multiple = (int(input("What Number? ")))
        self.wArray[row, :] = np.multiply(self.wArray[row, :],multiple) # Yes, you couse use *, but I like this for readablity
        return self.wArray

    def multiply_column(self):
        column = (int(input("Which column? ")) - 1)
        multiple = (int(input("What Number? ")))
        self.wArray[:, column] = np.multiply(self.wArray[:, column],multiple) # ":" means select all rows or columns depending on where it is placed
        return self.wArray
    
    def row_addition(self): # Might need subarrays, numpy doesnt seem to provide a way to add values within the same matrix
        I_row = (int(input("Row to be added to? ")) - 1)
        A_row = (int(input("Row added to other row? ")) - 1)
        A_row_multiple = int(input("What is 2nd row multplied by? "))
        self.addition_buffer_row_column = np.multiply(self.wArray[A_row, :], A_row_multiple)
        self.wArray[I_row, :] = np.array([term1 + term2 for term1, term2 in zip(self.wArray[I_row, :], self.addition_buffer_row_column)])
        self.addition_buffer_row_column = np.empty
        return self.wArray
    
    def col_addition(self):
        I_col = (int(input("column to be added to? ")) - 1)
        A_col = (int(input("column added to other column? ")) - 1)
        A_col_multiple = int(input("What is 2nd column multplied by? "))
        self.addition_buffer_row_column = np.multiply(self.wArray[:, A_col], A_col_multiple)
        self.wArray[:, I_col] = np.array([term1 + term2 for term1, term2 in zip(self.wArray[:, I_col], self.addition_buffer_row_column)])
        self.addition_buffer_row_column = np.empty
        return self.wArray

    def row_subtraction(self):
        I_row = (int(input("Row to be subtracted from? ")) - 1)
        A_row = (int(input("Row used to subtract? ")) - 1)
        A_row_multiple = int(input("What is 2nd row multplied by? "))
        self.subtraction_buffer_row_column = np.multiply(self.wArray[A_row, :], A_row_multiple)
        self.wArray[I_row, :] = np.array([term1 - term2 for term1, term2 in zip(self.wArray[I_row, :], self.subtraction_buffer_row_column)])
        self.subtraction_buffer_row_column = np.empty
        return self.wArray
    
    def col_subtraction(self): 
        I_col = (int(input("column to be subtracted from? ")) - 1)
        A_col = (int(input("column used to subtract? ")) - 1)
        A_col_multiple = int(input("What is 2nd col multplied by? "))
        self.subtraction_buffer_row_column = np.multiply(self.wArray[:, A_col], A_col_multiple)
        self.wArray[:, I_col] = np.array([term1 - term2 for term1, term2 in zip(self.wArray[:, I_col], self.subtraction_buffer_row_column)])
        self.subtraction_buffer_row_column = np.empty
        return self.wArray
    
    def deter_finder(self):
        return int(np.linalg.det(self.wArray))
    
    # def inv_finder(): # Will give floats, not sure how to solve

def makeMatrix():
    inputNums = list(map(int, input('Input RxC, Ex: "R C"\n').split()))
    while len(inputNums) < 2: # Input validation 
        inputNums = list(map(int, input('Input RxC, Ex: "R C"\n').split()))
    row, column = inputNums[0], inputNums[1] 
    tempMatrix = matrix(row, column)
    tempMatrix.reshape_and_fill()
    ### print(tempMatrix.wArray)
    return tempMatrix

def printMatrix():
    printString = "["
    nums = globalMatrix.wArray.shape
    rows = nums[0]
    cols = nums[1]
    for i in range(rows):
        printString = printString + "\n"
        for j in range(cols):
            printString = printString + str(globalMatrix.wArray[i][j]) + " "
    printString = printString + "\n]"
    print(printString)

def start():
    global globalMatrix
    globalMatrix = makeMatrix()
    printMatrix()

start()