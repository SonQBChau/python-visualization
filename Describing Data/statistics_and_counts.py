import pandas as pd

names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("./data/adult.data", header=None, names=names)

# GATHERING STATISTICS ON DATA 
print(train_df.describe())

# FINDING THE DATA TYPES
print(train_df.info())  # Use the info() function on the dataframe

# CONVERTING DATA TYPES
train_df['numeric_column'] = pd.to_numeric(train_df['age'])
print(train_df.head())

# FINDING UNIQUE VALUES
print(train_df['relationship'].unique())
print(train_df['relationship'].value_counts())

# GROUPING THE DATA
# This function takes a list of columns by which you would like to group your dataframe. 
# It then performs the requested calculations on each group individually and returns the results by group      
# Group by relationship and then get the value counts of label with normalization             
# We can see that 55% of husbands make more than 50k
print(train_df.groupby('relationship')['label'].value_counts(normalize=True))

# see the mean hours worked per week by workclass
# Federal government workers work more than local workers on average. 
# Never-worked average about 28 hours
print(train_df.groupby(['workclass'])['hoursperweek'].mean())

# FINDING THE CORRELATION
# there is a higher correlation between “hours per week” and “education num”
print(train_df.corr())
# Convert the string label into a value of 1 when >= 50k and 0 otherwise
train_df['label_int'] = train_df.label.apply(lambda x: ">" in x)
print(train_df.corr())

# GENERATING PERCENTILES
# Use the describe function to calculate the percentiles specified                     
print(train_df.describe(percentiles=[.01,.05,.95,.99]))