import pandas as pd

names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("./data/adult.data", header=None, names=names)

# Gathering statistics on data 
print(train_df.describe())

# Read in data as explained in reading CSV lesson
print(train_df.info())  # Use the info() function on the dataframe

# Converting data types
# to_numeric()
# to_datetime()
# to_string()
train_df['numeric_column'] = pd.to_numeric(train_df['age'])
print(train_df.head())

# Finding unique values
print(train_df['relationship'].unique())
print(train_df['relationship'].value_counts())