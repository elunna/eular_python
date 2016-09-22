import unittest
import matrix


class TestMatrix(unittest.TestCase):
    # Tests for read_matrix(filename):
    # Reading just 0 in a file, returns 1x1 matrix with 0
    def test_readmatrix_1x1file_1x1matrix(self):
        expected = [[0]]
        result = matrix.read_matrix('test_matrix1.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_2x2file_zerofilled_2x2matrix(self):
        expected = [[1, 2], [3, 4]]
        result = matrix.read_matrix('test_matrix2.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_2x2file_nonfilled_2x2matrix(self):
        expected = [[1, 2], [3, 4]]
        result = matrix.read_matrix('test_matrix3.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_3x3file_zerofilled_3x3matrix(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = matrix.read_matrix('test_matrix4.txt')
        self.assertEqual(expected, result)

    # Tests for print_matrix(matrix):
    def test_printmatrix_1x1(self):
        expected = '00\n'
        m = matrix.read_matrix('test_matrix1.txt')
        result = matrix.print_matrix(m)
        self.assertEqual(expected, result)

    def test_printmatrix_2x2file_zerofilled(self):
        expected = '01 02\n03 04\n'
        m = matrix.read_matrix('test_matrix2.txt')
        result = matrix.print_matrix(m)
        self.assertEqual(expected, result)

    def test_printmatrix_2x2file_nonfilled(self):
        expected = '01 02\n03 04\n'
        m = matrix.read_matrix('test_matrix3.txt')
        result = matrix.print_matrix(m)
        self.assertEqual(expected, result)

    # Tests for extract_line(matrix, point, xyincrement) are implicit since get_rows,
    # get_columns, get_right_diagonals, get_right_diagonals use extract_line.

    # Tests get_rows(matrix):
    def test_getrows_3x3_returns3lists(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = matrix.read_matrix('test_matrix4.txt')
        result = matrix.get_rows(m)
        self.assertEqual(expected, result)

    # Tests get_columns(matrix):
    def test_getcolumns_3x3_returns3lists(self):
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        m = matrix.read_matrix('test_matrix4.txt')
        result = matrix.get_columns(m)
        self.assertEqual(expected, result)

    # Tests get_right_diagonals(matrix):
    def test_get_right_diagonals_3x3_returns5lists(self):
        expected = [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
        m = matrix.read_matrix('test_matrix4.txt')
        result = matrix.get_right_diagonals(m)
        self.assertEqual(expected, result)

    # Tests get_left_diagonals(matrix):
    def test_get_left_diagonals_3x3_returns5lists(self):
        expected = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
        m = matrix.read_matrix('test_matrix4.txt')
        result = matrix.get_left_diagonals(m)
        self.assertEqual(expected, result)

    # Tests for scan_matrix_lines(matrix):
    # In this order: rows, columns, right diagonals, left diagonals.
    def test_scanmatrixlines_3x3_returns16lists(self):
        expected = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [7], [4, 8], [1, 5, 9], [2, 6], [3],
            [1], [2, 4], [3, 5, 7], [6, 8], [9]
        ]
        m = matrix.read_matrix('test_matrix4.txt')
        result = matrix.scan_matrix_lines(m)
        self.assertEqual(expected, result)