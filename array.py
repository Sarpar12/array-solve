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
    for count, values in enumerate(filled_matrix):
        row_number = count + 1
        for count2, values2 in enumerate(filled_matrix):
            column_number = count2 + 1
            filled_matrix[count][count2] = int(input('Number for row ' + str(row_number) + ' and column ' + str(column_number) + '? '))
            print(filled_matrix)

populate()