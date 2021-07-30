import numpy as np
from scipy import stats

def perform_calculations(array):
    np_array = np.array(array)
    max = np.max(array)
    std = np.std(np_array)
    sum = np.sum(np_array)
    dot = np.dot(np_array, np_array)
    return max, std, sum, dot  # Replace with max, std, sum, and dot product


# calling the function and printing result
print(perform_calculations(np.random.rand(5)))


def correlation(array1, array2):
    array_1 = np.array(array1)
    array_2 = np.array(array2)
    correlation = stats.pearsonr(array_1, array_2)
  
    # Replace with a tuple containing (correlation, p-value)
    return correlation


# calling the function and printing result
print(correlation(np.random.rand(5), np.random.rand(5)))
