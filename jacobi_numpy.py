import numpy as np
from prettytable import PrettyTable

table = PrettyTable()

class JacobiMethod:
	def __init__(self, coeff_matrix, const_vector):
		self.coeff_matrix = np.array(coeff_matrix)
		self.const_vector = np.array(const_vector)
		self.solution = np.array([0., 0., 0.]) 
		
	def calculate(self):
		n = self.solution.shape[0]
		
		table.field_names = [f'x{i}' for i in range(1, n+1)]
		
		while True:
			table.add_row([f'{value:.5f}' for value in self.solution])
			x_new = np.zeros_like(self.solution)
			for i in range(n):
				_sum = 0
				for j in range(n):
					if not i == j:
						_sum -= self.coeff_matrix[i][j] * self.solution[j] 
					else:
						_sum += self.const_vector[i]		
				x_new[i] = _sum / self.coeff_matrix[i][i]
			if max(abs(np.array(self.solution)-np.array(x_new))) < 0.00005:
				break
			self.solution = x_new
		
		print(table)		
	
	
A = np.array([
	[2., -1., 0.],
    [-1., 3., -1.],
    [0., -1., 2.],
])
              
# R.H.S. Vector
b = np.array([1., 8., -5.])

jm = JacobiMethod(A, b)
jm.calculate()
		
