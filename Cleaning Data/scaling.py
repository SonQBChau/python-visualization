from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

# Create a matrix of data
data = [[-1, 2], 
        [-0.5, 6], 
        [0, 10], 
        [1, 18]]

print("Before Standard scaling")
print(np.mean(data, 0))
print(np.std(data, 0))

####################
# STANDARD SCALING #
####################
# Standard scaling subtracts the mean and divides by the standard deviation. 
# This centers the feature on zero with unit variance

# Initalize a StandardScaler
standard = StandardScaler()
# Fit and transform the data with the StandardScaler
standard_data = standard.fit_transform(data)

print("After Standard scaling")
print(np.mean(standard_data, 0))
print(np.std(standard_data, 0))

###################
# MIN/MAX SCALING #
###################
# Create matrix of data
data = [[-1, 2], 
        [-0.5, 6], 
        [0, 10], 
        [1, 18]]

# Initalize MinMaxScaler
min_max = MinMaxScaler()
# Fit and transform the data
min_max_data = min_max.fit_transform(data)

print(np.min(min_max_data, 0))
print(np.max(min_max_data, 0))
print(np.mean(min_max_data, 0))
print(np.std(min_max_data, 0))