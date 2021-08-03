import numpy as np
import pandas as pd
import pandas.util.testing as tm; tm.N = 3

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
# Crosstab with normalized outputs
print(pd.crosstab(train_df['label'], train_df.relationship, normalize=True))

# RESHAPE
def unpivot(frame):
    N, K = frame.shape
    data = {'value' : frame.values.ravel('F'),
            'variable' : np.asarray(frame.columns).repeat(N),
            'date' : np.tile(np.asarray(frame.index), K)}
    return pd.DataFrame(data, columns=['date', 'variable', 'value'])
df = unpivot(tm.makeTimeDataFrame())
print(df.head())