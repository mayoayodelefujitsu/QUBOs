import numpy as np

path = 'TSP//bays29.npz'

data = np.load(path)
cost_function = data['objective']
constraint_function = data['constraint']
print(cost_function)
print(constraint_function)


