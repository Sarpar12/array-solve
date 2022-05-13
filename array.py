from array import *

def matrix_create():
        
    m = int(input('How many columns? '))        # This is taking inputs for number of rows and columns
    print('You input ' + str(m) + ' columns.' )
    n = int(input('How many rows? '))
    print('You input' + str(n) + 'rows.' )
    
    array1 = [0] * n       # This creates the matrix
    for i in range (n):
        array1[i] = [0] * m 
    print(array1)

matrix_create() 

        



    

