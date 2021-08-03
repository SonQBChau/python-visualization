import numpy as np
import pandas as pd
# we added 3 missing values with np.nan
pd_series = pd.Series([5, 10, np.nan, 15, 20, np.nan, 25, 50, np.nan])
print(pd_series)
print("Average of non-missing values: {0}".format(pd_series.mean()))

#############################
# USING A STATISTICAL VALUE #
#############################
# Fill the missing values with mean value
pd_series = pd_series.fillna(pd_series.mean())
print(pd_series)

#################
# USING A MODEL #
#################
# A popular algorithm for this is K-Nearest Neighbor

######################################
# TRACKING AND DROPPING MISSING DATA #
######################################
# Create a series with missing data
pd_series = pd.Series([5, 10, np.nan, 15, 20, np.nan, 25, 50, np.nan])
# Drop rows with missing data
pd_series = pd_series.dropna()
print(pd_series)

# Create a series with missing values
pd_series = pd.Series([5, 10, np.nan, 15, 20, np.nan, 25, 50, np.nan])
# Show which rows are missing
print(pd_series.isnull())