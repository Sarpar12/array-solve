"""
Contains the main implementation of the program
"""
import sys
from typing import List
from src.array import Matrix, MatrixStorage, MatrixWrapper

def create_matrix_wrapper(rows: int | None = None, cols: int | None = None, filename: str | None = None) -> MatrixWrapper:
    """
    Creates a MatrixWrapper. If a filename is specified, reads from that file.
    If not, user input will be read in and converted. For example:

    ```python
    create_matrix(2, 2, "input.txt")
    create_matrix(2, 2)
    ```

    `params:`
        rows {int}: the amount of rows, optional if filename is given
        cols {int}: the amount of columns, optional if filename is given
        filename {str}: the filename to read from, optional

    `returns:` 
        a Matrix object
    
    `raises:` 
        SyntaxError if a a filename is not provided and rows and cols also aren't provided
        ValueError if a input value can't be converted into a float
    """
    if filename is not None:
        with open(filename, 'r', encoding='UTF-8') as file:
            lines = [line.strip().split() for line in file.readlines()]
            if not rows:
                rows = len(lines)
            if not cols:
                cols = len(lines[0])
            float_list = [float(num) for line in lines for num in line.split()]
    else:
        if rows is None or cols is None:
            raise SyntaxError("Rows and columns must be specified for manual input.")
        matrix_values : List[str] = input("Enter the matrix values separated by spaces:\n").split()
        float_list = [float(num) for num in matrix_values]
    matrix = Matrix(rows, cols, float_list)
    matrix_stack = MatrixStorage(matrix)
    return MatrixWrapper(matrix, matrix_stack) 

def display_matrices(matrix_wrapper_list : List[MatrixWrapper])  -> None:
    """
    displays the matrices in matrix_list, either in full or a preview, depending on the length

    `params:` 
        matrix_list {List[Matrix]} : a list of Matrix objects
    """
    for index, matrix_wrapper in enumerate(matrix_wrapper_list):
        m_row = matrix_wrapper.matrix.rows
        m_col = matrix_wrapper.matrix.columns
        if m_row < 16 and m_col < 16:
            print(f"Matrix Index {index}: {matrix_wrapper}")
        else:
            print(f"Matrix Index {index}: {matrix_wrapper[0:16]}")

def do_operation(matrix_wrapper : MatrixWrapper, operation_value : int) -> None:
    """
    Does the specified operation found in main()

    `params:` 
        matrix {Matrix} : a Matrix object
        operation_value {int} : a int
        matrix_stack {MatrixStorage} : a MatrixStorage object

    `raises:`
        ValueError if a operation_value isn't found
    """
    m_stack : MatrixStorage = matrix_wrapper.stack
    matrix : Matrix = matrix_wrapper
    match operation_value:
        case 2:
            # Undoes an operation
            matrix.set_array(m_stack.get_prev_matrix())
            return
        case 3:
            # Multiplies a row
            matrix.multiply_row()
            return
        case 4:
            # Multiples a colum
            matrix.multiply_column()
            return
        case 5:
            # Adds one row to another
            matrix.row_addition()
            return
        case 6:
            # Adds one column to another
            matrix.col_addition()
            return
        case 7:
            # Subtract one row from another
            matrix.row_subtraction()
            return
        case 8:
            # subtracts one col from another
            matrix.col_subtraction()
            return
        case 9: 
            # transposes the matrix
            matrix.transpose()
            return
        case 10:
            # Finds determinant
            print(f"Determinant: {matrix.deter_finder()}")

def main():
    """
    gets initial matrix, contains the loop that runs the program
    """
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("python main.py <rows> <count> <filename | Optional>")
        exit(1)
    elif len(sys.argv) == 3:
        matrix_wrapper : MatrixWrapper = create_matrix_wrapper(int(sys.argv[1]), int(sys.argv[2]))
    else:
        matrix_wrapper : MatrixWrapper = create_matrix_wrapper(int(sys.argv[1]), int(sys.argv[2]), sys.argv(3))
    matrix_wrapper_list : List[MatrixWrapper] = [].append(matrix_wrapper)
    selected_matrix : MatrixWrapper = matrix_wrapper_list[0]
    while True:
        input_val : int = int(input(
        """
        0) Add Matrix
        1) Select Matrix
        2) Undo Operation
        3) Multiply Row            
        4) Multiply Column
        5) Add Row to another
        6) Add column to another
        7) Subtract row from another
        8) Subtract col from another
        9) Transpose Matrix
        10) Find Determinant  
        """))
        match input_val:
            case 0:
                input_matrix_dim : str = input("Please enter <row> <col> <filename | Optional>")
                if len(input_matrix_dim == 1):
                    new_matrix : MatrixWrapper = create_matrix_wrapper(input_matrix_dim)
                elif len(input_matrix_dim) == 2:
                    new_matrix : MatrixWrapper = create_matrix_wrapper(int(input_matrix_dim[0]), int(input_matrix_dim[1]))
                elif len(input_matrix_dim) == 3:
                    new_matrix : MatrixWrapper = create_matrix_wrapper(int(input_matrix_dim[0]), int(input_matrix_dim[1]), input_matrix_dim[2])
                matrix_wrapper_list.append(new_matrix)
            case 1:
                display_matrices(matrix_wrapper_list)
                matrix_index : int = int(input("Which matrix?"))
                try:
                    selected_matrix = matrix_wrapper_list[matrix_index]
                except IndexError:
                    print(f"Selected Index {selected_matrix} isn't in the list!")
            case _:
                break
        try:
            do_operation(selected_matrix, input_val)
        except ValueError:
            print(f"That operation ({input_val}) isn't supported!")
        print(selected_matrix)

if __name__ == "__main__":
    main()
