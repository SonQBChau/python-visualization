import pandas as pd # calling pandas module

def read_csv():

    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("./data/auto-mpg.data", header=None, names=names, delim_whitespace=True)
    print(df.head())
    return df.shape

# Calling the function and printing the result
print(read_csv())