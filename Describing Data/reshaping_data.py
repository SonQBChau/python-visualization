import numpy as np
import pandas as pd
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("adult.data", header=None, names=names)

# Pivot the data frame to show by relationship, workclass (rows) and label (columns) the average hours per week.
print(pd.pivot_table(train_df, values='hoursperweek', index=['relationship','workclass'], 
               columns=['label'], aggfunc=np.mean).round(2))