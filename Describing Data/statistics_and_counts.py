import pandas as pd

names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("./data/adult.data", header=None, names=names)

# Gathering statistics on data 
print(train_df.describe())

# Read in data as explained in reading CSV lesson
print(train_df.info())  # Use the info() function on the dataframe

# Converting data types
train_df['numeric_column'] = pd.to_numeric(train_df['age'])
print(train_df.head())

# Finding unique values
print(train_df['relationship'].unique())
print(train_df['relationship'].value_counts())

# This function takes a list of columns by which you would like to group your dataframe. 
# It then performs the requested calculations on each group individually and returns the results by group      
# Group by relationship and then get the value counts of label with normalization             
# We can see that 55% of husbands make more than 50k
print(train_df.groupby('relationship')['label'].value_counts(normalize=True))

# see the mean hours worked per week by workclass
# Federal government workers work more than local workers on average. 
# Never-worked average about 28 hours
print(train_df.groupby(['workclass'])['hoursperweek'].mean())
