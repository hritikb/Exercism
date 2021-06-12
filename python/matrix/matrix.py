class Matrix:
    matrix = []
    def __init__(self, matrix_string):
        global matrix
        matrix = matrix_string.split('\n')

    def row(self, index):
        global matrix
        rowchar = matrix[index - 1]
        row = [int(i) for i in rowchar.split()]
        return row

    def column(self, index):
        global matrix
        mat = [m.split() for m in matrix]
        col = [int(i[index - 1]) for i in mat]
        return col
