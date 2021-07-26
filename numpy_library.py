import numpy as np

#############################
# SINGLE DIMENSIONAL ARRAYS #
#############################

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

##########################
# TWO DIMENSIONAL ARRAYS #
##########################
# Create 2d array
print("--0--")
np_2d_array = np.array([[1,2,3], 
                        [4,5,6]])
print(np_2d_array)

# Calculate the transpose, which is when you swap the columns and rows.
print("--1--")
np_2d_array_T = np_2d_array.T
print(np_2d_array_T)

# Print the shape of the array as (number of rows, number of columns)
print("--3--")
print(np_2d_array.shape)

# Access elements in the 2d array by index. 
# First index is the row number
# Second index is the column number
# Index numbers start from 0
print("--4--")
print(np_2d_array[1,1])
print(np_2d_array[0,2])

###########################
# CALCULATING DOT PRODUCT #
###########################
np_array = np.array([5, 10, 15, 20, 25, 30])
dot_product = np.dot(np_array, np_array)
print(dot_product)

############################
# GENERATING RANDOM VALUES #
############################
# Generage a single random number in range [0,1)
print("--0--")
print(np.random.rand())

# Generate a matrix of random numbers in range [0,1) with shape (3,2)
print("--1--")
print(np.random.rand(3,2))