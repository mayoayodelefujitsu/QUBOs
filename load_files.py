import numpy as np

path = 'TSP//gr17.npz'

data = np.load(path)
cost_function_qubo_matrix = data['cost_function_qubo']
cost_function_constant= data['cost_function_constant']
constraint_function_qubo_matrix = data['constraint_function_qubo']
constraint_function_constant= data['constraint_function_constant']

print('constant term and QUBO matrix representing the cost (unconstrained objective) function' )
print(cost_function_constant, cost_function_qubo_matrix)
print('constant term and QUBO matrix representing the constraint function' )
print(constraint_function_constant, constraint_function_qubo_matrix)


