import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights = sns.load_dataset("flights")
# Subset the data to years >= 1956 to more easily fit on the plot
flights = flights[flights.year >= 1956]

'''
``data`` which is the first parameter and specifies the dataframe to use.
``row`` which is the column name from your dataframe you want to use as the rows of your grid.
``col`` which is the column name from your dataframe you want to use as the columns of your grid.
``margin_titles`` which if True, the titles for the row variable are drawn to the right of the last column.
'''
g = sns.FacetGrid(flights, row="year", margin_titles=True)
'''
``func`` which is the first argument and is the plotting function you wish to use.
``args`` is the second parameter and is the column name for the variable you wish to plot.
``color`` which allows you to specify the plot color.
'''
g.map(plt.plot, "passengers", color="steelblue")
plt.show()