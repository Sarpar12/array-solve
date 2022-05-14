from array import *

class matrix:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.array1 = []


    def create(self):

        self.array1 = [0] * self.columns       # This creates the matrix
        for i in range (self.columns):
            self.array1[i] = [0] * self.rows
        

def init_value():
    rows = int(input("How many rows? "))
    columns = int(input("How many columns? "))
    matrices1 = matrix(rows, columns)
    matrices1.create()
    return matrices1.array1

init_value()

def row_switch():
    row1 = input("Row 1? ")
    row2 = input("Row 2? ")
