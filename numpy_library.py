import numpy as np

# This creates our array
np_array = np.array([5, 10, 15, 20, 25, 30])
print("--0--")

# Gets the unique values
print(np.unique(np_array))
print("--1--")

# Calculates the standard deviation
print(np.std(np_array))
print("--2--")

# Calculates the maximum
print(np_array.max())
print("--3--")

# Squares each value in the array
print(np_array ** 2)
print("--4--")

# Adds the arrays together element wise
print(np_array + np_array)
print("--5--")

# The sum of the squares of the elements
print(np.sum(np_array ** 2))
print("--6--")

# Gives you the shape: (rows, columns)
print(np_array.shape)