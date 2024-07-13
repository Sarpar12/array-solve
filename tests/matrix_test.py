"""
Module for testing if functionality works
"""

import unittest
from unittest.mock import patch
import numpy as np
from src.array import Matrix

def reset_matrix(matrix: Matrix):
    """
    resets matrix to blank slate
    """
    array : np.ndarray = np.arange(1, 10).reshape(3,3)
    matrix.set_array(array)

class TestMatrix(unittest.TestCase):
    """
    Testing class for testing matrix functionality
    """
    def setUp(self):
        self.rows = 3
        self.columns = 3
        self.float_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.matrix = Matrix(self.rows, self.columns, self.float_list)

    # pylint: disable=W0613
    @patch('builtins.input', side_effect=['1', '3'])  # Mocks input swapping column 1 with column 3
    def test_col_swap(self, mocked_input):
        """
        tests column swapping
        """
        print("Testing Column Swap")
        self.matrix.col_swap()
        expected_array = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
        np.testing.assert_array_equal(self.matrix.get_array(), expected_array)
        reset_matrix(self.matrix)

    @patch('builtins.input', side_effect=['2', '3'])  # Mocks input for multiplying column 2 by 3
    def test_multiply_column(self, mocked_input):
        """
        tests column multiplication
        """
        print("Testing Column Multiplication")
        self.matrix.multiply_column()
        expected_array = np.array([[1, 6, 3], [4, 15, 6], [7, 24, 9]])
        np.testing.assert_array_equal(self.matrix.get_array(), expected_array)

    @patch('builtins.input', side_effect=['1', '2', '3'])  # Mocks inputs for row addition
    def test_row_addition(self, mocked_input):
        """
        tests row addition
        """
        print("Testing Row Addition")
        self.matrix.row_addition()
        expected_array = np.array([[13, 17, 21], [4, 5, 6], [7, 8, 9]])
        np.testing.assert_array_equal(self.matrix.get_array(), expected_array)
        reset_matrix(self.matrix)

    @patch('builtins.input', side_effect=['1', '2', '2'])  # Mocks inputs for column addition
    def test_col_addition(self, mocked_input):
        """
        tests column addition
        """
        print("Testing Column Addition")
        self.matrix.col_addition()
        expected_array = np.array([[5, 2, 3], [14, 5, 6], [23, 8, 9]])
        np.testing.assert_array_equal(self.matrix.get_array(), expected_array)
        reset_matrix(self.matrix)

    @patch('builtins.input', side_effect=['1', '2', '2'])  # Mocks inputs for row subtraction
    def test_row_subtraction(self, mocked_input):
        """
        tests row subtraction 
        """
        print("Testing Row Subtraction")
        self.matrix.row_subtraction()
        expected_array = np.array([[-7, -8, -9], [4, 5, 6], [7, 8, 9]])
        np.testing.assert_array_equal(self.matrix.get_array(), expected_array)
        reset_matrix(self.matrix)

    @patch('builtins.input', side_effect=['1', '2', '2'])  # Mocks inputs for column subtraction
    def test_col_subtraction(self, mocked_input):
        """
        tests column subtraction 
        """
        print("Testing Column Subtraction")
        self.matrix.col_subtraction()
        expected_array = np.array([[-3, 2, 3], [-6, 5, 6], [-9, 8, 9]])
        np.testing.assert_array_equal(self.matrix.get_array(), expected_array)
        reset_matrix(self.matrix)

    def test_determinant(self):
        """
        tests determinant
        """
        print("Testing Determinant of 3x3")
        expected_det = np.linalg.det(np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]]))
        result_det = Matrix(3, 3, [1, 2, 3, 0, 1, 4, 5, 6, 0]).deter_finder()
        self.assertAlmostEqual(result_det, expected_det, msg="Determinant of matrix is incorrect.")

    def test_determinant_singular_matrix(self):
        """
        tests determinant
        """
        print("tests determinant of singular matrix:")
        singular_matrix = Matrix(2, 2, [2, 4, 1, 2])  # This matrix is singular, det should be 0.
        result_det = singular_matrix.deter_finder()
        self.assertEqual(result_det, 0, msg="Determinant of singular matrix should be 0.")

    def test_transpose(self):
        """
        tests transposing
        """
        print("Testing matrix transposition")
        self.matrix.transpose()
        expected_array = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        np.testing.assert_array_equal(self.matrix.get_array(), expected_array)
        reset_matrix(self.matrix)

    def test_cofactor_index(self):
        """
        tests cofactor of an index
        """
        print("Testing cofactor of an index")
        self.matrix.set_array(np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]]))
        cofactor = self.matrix.cofactor_index(1, 1)  # Cofactor of the first element
        expected_cofactor = float(-24)  # Calculated using minor and cofactor definition
        self.assertAlmostEqual(cofactor, expected_cofactor)

    def test_cofactor_matrix(self):
        """
        tests cofactor matrix
        """
        print("Testing cofactor matrix")
        self.matrix.set_array(np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]]))
        cofactor_matrix = self.matrix.cofactor_matrix()
        expected_matrix = np.array([[-24, 20, -5], [18, -15, 4], [5, -4, 1]])
        np.testing.assert_array_almost_equal(cofactor_matrix, expected_matrix)
        
    def test_adjoint_matrix(self):
        """
        tests the adjoint_matrix() function
        """
        print("Testing adjoint matrix:")
        org_matrix = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 1, 9])
        result_matrix = org_matrix.adjoint_matrix()
        expected_matrix = np.array([[39, -15, -3], [6, -12, 6], [-31, 13, -3]])
        np.testing.assert_array_almost_equal(result_matrix, expected_matrix)
        

if __name__ == '__main__':
    unittest.main()
