import numpy as np


def perform_calculations(array):
    np_array = np.array(array)
    max = np_array.max()
    std = np.std(np_array)
    sum = np.sum(np_array)
    dot = np.dot(np_array, np_array)
    return max, std, sum, dot  # Replace with max, std, sum, and dot product
