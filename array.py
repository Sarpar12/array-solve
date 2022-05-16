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

def populate():     # Fills matrix with values
    for count, values in enumerate(filled_matrix):      # Values refer to a list inside a list like [x, y] in [[x, y], [z, x]]
        row_number = count + 1
        for count2, values2 in enumerate(values):       # values2 refer to the objects inside value([x, y])
            column_number = count2 + 1
            filled_matrix[count][count2] = int(input('Number for row ' + str(row_number) + ' and column ' + str(column_number) + '? '))
            print(filled_matrix)

def row_swap(row1, row2):
    Actual_row1 = row1 - 1
    Actual_row2 = row2 - 1
    filled_matrix[Actual_row1], filled_matrix[Actual_row2] = filled_matrix[Actual_row2], filled_matrix[Actual_row1]
    return filled_matrix

def multiply(row, number):
    Actual_row = row - 1
    filled_matrix[Actual_row] = [i * 5 for i in filled_matrix[Actual_row]]      # This uses lists comprehension
    return filled_matrix

def subtract(row1, row2):
    Actual_row1 = row1 - 1
    Actual_row2 = row2 - 1
    filled_matrix[Actual_row1] = [a - b for a, b in zip(filled_matrix[Actual_row1], filled_matrix[Actual_row2])]
            # Basically, f_m[A_R1] = A, which has [a, a, a,] and f-m[A_R2] = B which has [b, b, b], so you can subtract
    return filled_matrix

def addition(row1, row2):
    Actual_row1 = row1 - 1
    Actual_row2 = row2 - 1
    filled_matrix[Actual_row1] = [a + b for a, b in zip(filled_matrix[Actual_row1], filled_matrix[Actual_row2])]
            # Subtraction but you add instead of subtract. f_m = filled_matrix, A_R = actual_rows
    return filled_matrix

def display_matrix():
    print(*filled_matrix, sep = "\n")

while True: 
    init_value()
    populate()
    display_matrix()
    choice = int(input('\t1. Swap Rows\n\t2. Multiply\n\t3. Add\n\t4. Subtract\n\t5. Exit\n'))
    if choice == 1:
        row1 = int(input('Initial Row? '))
        row2 = int(input('With which row? '))
        row_swap(row1, row2)
        display_matrix()
    elif choice == 2:
        row = int(input('Which Row? '))
        number = int(input('By how much? '))
        multiply(row, number)
        display_matrix()
    elif choice == 3:
        row1 = int(input('Which row are you adding to(Inital Row)? '))
        row2 = int(input('Which row is being added to the Initial Row? '))
        addition(row1, row2)
        display_matrix()
    elif choice == 4:
        row1 = int(input('Which row are you subtracting from(Inital Row)? '))
        row2 = int(input('Which row is Initial Row being subtracted by? '))  
        subtract(row1, row2)
        display_matrix()    
    elif choice == 5:
        exit()  
