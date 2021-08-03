import seaborn as sns            # importing seaborn functionality    
import pandas as pd
import matplotlib.pyplot as plt
 
flights_long=sns.load_dataset("flights")   # importing dataset
print(flights_long)
# filtering the dataset to obtain the January records for all years
flights_long=flights_long[flights_long.month == 'Jan']
print(flights_long)
#plotting a line graph
plot=sns.lineplot(flights_long.year, flights_long.passengers)
plt.show()
