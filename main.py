from src.array import Matrix, MatrixStorage
import sys
from typing import List

def create_matrix(rows: int | None = None, cols: int | None = None, filename: str | None = None) -> Matrix:
    """
    Creates a matrix. If a filename is specified, reads from that file.
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
    return Matrix(rows, cols, float_list)

def create_storage(matrix: Matrix | None = None) -> MatrixStorage:
    """
    Creates a matrix stack

    `params:` 
        matrix: a Matrix object, optional    

    `returns:`
        a MatrixStorage object
    """
    if matrix is not None:
        matrix_stack = MatrixStorage(matrix)
        return matrix_stack
    else:
        return MatrixStorage()
    
def display_matrices(matrix_list : List[Matrix])  -> None:
    """
    displays the matrices in matrix_list, either in full or a preview, depending on the length

    `params:` 
        matrix_list {List[Matrix]} : a list of Matrix objects
    """
    for index, matrix in enumerate(matrix_list):
        m_row = matrix.rows
        m_col = matrix.columns
        if m_row < 16 and m_col < 16:
            print(f"Matrix Index {index}: {matrix}")
        else:
            print(f"Matrix Index {index}: {matrix[0:16]}")

# def do_operation(matrix : Matrix, matrix_stack : MatrixStorage, operation_value : int) -> None:
#     """
#     Does the specified operation found in main()

#     `params:` 
#         matrix {Matrix} : a Matrix object
#         operation_value {int} : a int
#         matrix_stack {MatrixStorage} : a MatrixStorage object

#     `raises:`
#         ValueError if a operation_value isn't found
#     """
#     match operation_value:
#         case 1:

def main():
    """
    gets initial matrix, contains the loop that runs the program
    """
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("python main.py <rows> <count> <filename | Optional>")
        exit(1)
    elif len(sys.argv) == 3:
        matrix : Matrix = create_matrix(int(sys.argv[1]), int(sys.argv[2]))
    else:
        matrix : Matrix = create_matrix(int(sys.argv[1]), int(sys.argv[2]), sys.argv(3))
    matrix_list : List[Matrix] = [].append(matrix)
    selected_matrix : Matrix = matrix_list[0]
    matrix_stack : MatrixStorage = create_storage(None)
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
                    new_matrix : Matrix = create_matrix(input_matrix_dim)
                elif len(input_matrix_dim) == 2:
                    new_matrix : Matrix = create_matrix(int(input_matrix_dim[0]), int(input_matrix_dim[1]))
                elif len(input_matrix_dim) == 3:
                    new_matrix : Matrix = create_matrix(int(input_matrix_dim[0]), int(input_matrix_dim[1]), input_matrix_dim[2])
                matrix_list.append(new_matrix)
            case 1:
                display_matrices(matrix_list)
                matrix_index : int = int(input("Which matrix?"))
                try:
                    selected_matrix = matrix_list[matrix_index]
                except IndexError:
                    print(f"Selected Index {selected_matrix} isn't in the list!")
        # try:
        #     do_operation(matrix, matrix_stack, input_val)
        # except ValueError:
        #     print(f"That operation ({input_val}) isn't supported!")

if __name__ == "__main__":
    main()
