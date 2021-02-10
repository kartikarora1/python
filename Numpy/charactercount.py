import numpy as np
x = np.array(['Python', 'PHP', 'JS', 'examples', 'html'])
print("\nArray:")
print(x)
print("Number of ‘P’:")
r = np.char.count(x, "P")
print(r)