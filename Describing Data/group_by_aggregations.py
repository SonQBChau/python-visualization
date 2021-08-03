import pandas as pd
def read_csv():
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("./data/auto-mpg.data", header=None, names=names, delim_whitespace=True)
    return df

df = read_csv() 

def group_aggregation(df, group_var, agg_var):
    return 0 # Update function to return the grouped data frame