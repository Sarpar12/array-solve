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
        

def init_value():       # Returns matrix with number of rows and columns filled with 0's as filled_matrix
    rows = int(input("How many rows? "))
    columns = int(input("How many columns? "))
    matrices1 = matrix(rows, columns)
    matrices1.create()
    global filled_matrix        # makes filled matrix a global variable
    filled_matrix = matrices1.array1        # takes array1 from filled_matrix, which was just filled with 0's

init_value()

def populate():
    for i in filled_matrix:
        row_number = row_number + 1
        n_o_t = (len(i) * -1)    # n_o_t stands for number of terms. len(i) is multiplied by -1 because the negative of len(i) will give the 0th index term
        if n_o_t <= -1:
            nth_term = (len(i) - (1 - len(i))) # nth term is the term number for number in a row, starting at index 1
            i[n_o_t] = input('Number for Term #' + str(nth_term) + 'in Row #' + str(row) + ' ?') 
            n_o_t = n_o_t + 1