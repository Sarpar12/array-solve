from array import *

class matrix:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.array1 = []


    def create(self):
        self.array1 = [0] * self.rows       # This creates the matrix
        for i in range (self.rows):
            self.array1[i] = [0] * self.columns
        

def init_value():       # Returns matrix with number of columns and rows filled with 0's as filled_matrix
    rows = int(input("How many rows? "))
    columns = int(input("How many columns? "))
    matrices1 = matrix(columns, rows)
    matrices1.create()
    global filled_matrix        # makes filled matrix a global variable
    filled_matrix = matrices1.array1        # takes array1 from filled_matrix, which was just filled with 0's

init_value()

def populate():     # Fills matrix with values
    for i in filled_matrix:     # i in this case is a list like [x, y, z, c] in [[x, y, z, c], [a, b, c, d], [q, w, e, r]]
        row_number = 0
        row_number = row_number + 1
        for j in i:     # j should refer to an element in a list such as [x] in [x, y, z, c]
            column_number = 0
            column_number = column_number + 1
            j = int(input('What is the value for Column ' + str(column_number) + ' in row ' + str(row_number) + '? '))

populate()