from scipy import stats
import numpy as np

array_1 = np.array([1,2,3,4,5,6])  # Create a numpy array from a list
array_2 = array_1  # Create another array with the same values

print(stats.pearsonr(array_1, array_2))  # Calculate the correlation which will be 1 since the values are the same 