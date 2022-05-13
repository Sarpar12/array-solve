from array import *

class initial_matrix:

    def __init__(self):
        self.array_i = [0]     # Creates Matrix upon init
        

    def matrix_create(self):
        
        m = int(input('How many columns? '))        # This is taking inputs for number of rows and columns
        print('You input' + m + 'columns.' )
        n = int(input('How many rows? '))
        print('You input' + n + 'rows.' )
        
       
        self.array1 = self.array_i * n       # This creates the matrix
        for i in range (n):
            self.array1[i] = self.array_i * m 

    

