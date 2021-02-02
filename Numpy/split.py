import numpy as np
x = np.array(['Python PHP Java C++'])
print("Original Array:")
print(x)
r = np.char.split(x)
print("\nSplit elements: ")
print(r)