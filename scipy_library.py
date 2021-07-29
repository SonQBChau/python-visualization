from scipy import stats
import numpy as np

############################
# CALCULATING CORRELATIONS #
############################

array_1 = np.array([1,2,3,4,5,6])  # Create a numpy array from a list
array_2 = array_1  # Create another array with the same values

print(stats.pearsonr(array_1, array_2))  # Calculate the correlation which will be 1 since the values are the same 

#######################
# NORMAL DISTRIBUTION #
#######################
x = stats.norm.rvs(loc=0, scale=10, size=10)  # Generate 10 values randomly sampled from a normal distribution with mean 0 and standard deviation of 10

print(x)

################################
# PROBABILITY DENSITY FUNCTION #
################################
p1 = stats.norm.pdf(x=-100, loc=0, scale=10)  # Get probability of sampling a value of -100
p2 = stats.norm.pdf(x=0, loc=0, scale=10)     # Get probability of sampling a value of 0

print(p1)
print(p2)

####################################
# CUMULATIVE DISTRIBUTION FUNCTION #
####################################
p1 = stats.norm.cdf(x=0, loc=0, scale=10)  # Get probability of sampling a value less than or equal to 0

print(p1)

######################################
# CALCULATING DESCRIPTIVE STATISTICS #
######################################
print(stats.describe(stats.norm.rvs(loc=0, scale=1, size=500)))  # Calculate descriptive statistics for 500 data points sampled from normal distribution with mean 0 and standard deviation of 1
