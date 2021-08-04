import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load data 
def read_csv():
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("./data/auto-mpg.data", header=None, names=names, delim_whitespace=True)
    return df

# Create the scatter plot
def scatter_plot(df):
    sns.lmplot(x="displacement", y="acceleration", data=df)
    sns.despine()
    plt.show()
    

# Call the function
scatter_plot(read_csv())

def bar_plot(df):
    #  filter out the data car_name would have ford
    df = df[df.car_name.str.contains('ford')]
    #  keeping all the rows for which model_year is 1975
    df = df[df["model_year"].isin([75])]

    # Create the bar plot
    sns.barplot(df['car_name'], df['cylinders'])
    sns.despine()
    plt.show()
    

# Call the function
bar_plot(read_csv())

def line_plot(df):
    # filtering the dataset to obtain ford car_name
    df=df[df.car_name.str.contains('ford')]
    #plotting a line graph
    sns.lineplot(df.model_year, df.weight)
    plt.show()
    

# Call the function
line_plot(read_csv())