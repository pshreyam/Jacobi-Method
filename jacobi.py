import numpy as np
from prettytable import PrettyTable

table = PrettyTable()

class JacobiMethod:
    def __init__(self, coeff_matrix, const_vector, initial=None, upper_limiting_error=0.00005):
        self.coeff_matrix = coeff_matrix
        self.const_vector = const_vector
        self.solution = initial or [0 for _ in self.const_vector]
        self.upper_limiting_error = upper_limiting_error

    def is_diag_dominant(self): 
        n = len(self.solution)

        for i in range(n):
            _sum = 0
            for j in range(n):
                if not i==j:
                     _sum = _sum + abs(self.coeff_matrix[i][j])
    
            if (abs(self.coeff_matrix[i][i]) < _sum):
                return False
    
        return True
    
    def handle_not_diag_dominant(self):   
        # Requires Implementation 
        print("Sorry! the system of equation is not diagonally dominant.")

    def calculate(self):
        if not self.is_diag_dominant():
            self.handle_not_diag_dominant()
            return

        n = len(self.solution)
        x_new = [0 for _ in self.solution]

        table.title = "Iteration Table"
        table.field_names = ['n', *[f'x{i}' for i in range(1, n+1)]]

        iteration = 1
        while True:
            table.add_row([iteration, *[f'{value:.5f}' for value in self.solution]])

            for i in range(n):
                _sum = 0
                for j in range(n):
                    if not i == j:
                        _sum -= self.coeff_matrix[i][j] * self.solution[j]
                _sum += self.const_vector[i]
                x_new[i] = _sum / self.coeff_matrix[i][i]

            if max(abs(np.array(self.solution)-np.array(x_new))) < self.upper_limiting_error:
                table.add_row([iteration+1, *[f'{value:.5f}' for value in x_new]])
                break

            self.solution = [round(x, 5) for x in x_new]
            iteration += 1

        print(table)
        print('\n Required Root : ', [f'{round(value,4):.4f}' for value in x_new])
# A = [[2, -1, 0],
#      [-1, 3, -1],
#      [0, -1, 2]]

# b = [1, 8, -5]

# jm = JacobiMethod(A, b)
# jm.calculate()
