import numpy as np
import pandas as pd
pd_series = pd.Series([5, 10, np.nan, 15, 20, np.nan, 25, 50, np.nan])
print("Average of non-missing values: {0}".format(pd_series.mean()))

# Fill the missing values wuth mean value
pd_series = pd_series.fillna(pd_series.mean())
print(pd_series)