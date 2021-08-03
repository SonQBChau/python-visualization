import seaborn as sns
import matplotlib.pyplot as plt

'''
-data: is the first parameter and is your matrix of data represented as a Panda’s dataframe.
-annot: if True will plot the actual data values in each cell.
-fmt: lets you control the string formatting. A value of “d” uses a decimal integer.
-linewidths: lets you set the width of the lines which separate each cell.
-ax: allows you to pass a custom Matplotlib Axes.
-cmap: allows you to pick the colormap to use when plotting.
'''
# Load dataset
flights_long = sns.load_dataset("flights")
# Pivot the dataset from long to wide format
flights = flights_long.pivot("month", "year", "passengers")
# Create a larger figure size to plot on
f, ax = plt.subplots(figsize=(12, 6))
# Create the heat map
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax, cmap='Blues')
plt.show()