import pandas as pd

names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("./data/adult.data", header=None, names=names)
# Gathering statistics on data 
print(train_df.describe())

# Read in data as explained in reading CSV lesson
print(train_df.info())  # Use the info() function on the dataframe