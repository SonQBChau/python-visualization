import numpy as np
import pandas as pd
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("./data/adult.data", header=None, names=names)

# PIVOT TABLE
# Pivot the data frame to show by relationship, workclass (rows) and label (columns) the average hours per week.
print(pd.pivot_table(train_df, values='hoursperweek', index=['relationship','workclass'], 
               columns=['label'], aggfunc=np.mean).round(2))

# CROSS TAB
# Calculate the frequencies between label and relationship
print(pd.crosstab(train_df['label'], train_df.relationship))