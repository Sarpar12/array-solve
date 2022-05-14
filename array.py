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
        print(self.array1)

mat1 = matrix(3, 3)
mat1.create()

