import numpy as np
x1 = np.array(['Python', 'PHP'])
x2 = np.array([' Java', ' C++'])
new_array = np.char.add(x1, x2)
print("new array:")
print(new_array)