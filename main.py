from src.array import Matrix, MatrixStorage
import sys

def create_matrix(rows: int, cols: int, filename: str | None) -> Matrix:
    """
    Creates a matrix. If a filename is specified, reads from that file.
    If not, user input will be read in and converted. For example:

    ```python
    create_matrix(2, 2, "input.txt")
    create_matrix(2, 2)
    ```

    `params:`
        rows {int}: the amount of rows
        cols {int}: the amount of columns
        filename {str}: the filename to read from, optional

    `returns:` 
        a Matrix object
    
    `raises:` 
        ValueError if a input value can't be converted into a float
    """
    if filename is not None:
        file = open(filename)
        float_list = [float(num) for num in file.read().split()]
        file.close()
    else:
        float_list = list(map(float, input("Matrix Values:\n")))
    return Matrix(rows, cols, float_list)

def create_storage(matrix: Matrix | None) -> MatrixStorage:
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