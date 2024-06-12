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
        matrixStack = MatrixStorage(matrix)
        return matrixStack
    else:
        return MatrixStorage()

def main():
    if len(sys.argv) != 3:
        print("python main.py <rows> <count>")
        exit(1)
    else: 
        print("testing")


if __name__ == "__main__":
    main()