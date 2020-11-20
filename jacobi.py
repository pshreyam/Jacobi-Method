import numpy as np
from prettytable import PrettyTable

table = PrettyTable()

class JacobiMethod:
	def __init__(self, coeff_matrix, const_vector, initial=None, tolerance=0.00005):
		self.coeff_matrix = coeff_matrix
		self.const_vector = const_vector
		self.solution = initial or [0 for _ in self.const_vector] 
		self.tolerance = tolerance
		
	def calculate(self):
		n = len(self.solution)
		x_new = [0 for i in self.solution]

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
					else:
						_sum += self.const_vector[i]		
				x_new[i] = _sum / self.coeff_matrix[i][i]
				
			if max(abs(np.array(self.solution)-np.array(x_new))) < self.tolerance:
				break
				
			self.solution = [round(x, 5) for x in x_new]
			iteration += 1

		print(table)		

		
# A = [[2, -1, 0],
#      [-1, 3, -1],
#      [0, -1, 2]]

# b = [1, 8, -5]

# jm = JacobiMethod(A, b)
# jm.calculate()