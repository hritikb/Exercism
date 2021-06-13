class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')
        self.matrix = [i.split() for i in self.matrix]
        self.matrix = [[int(i) for i in j] for j in self.matrix]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.matrix]

