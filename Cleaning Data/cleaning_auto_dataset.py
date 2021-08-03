import pandas as pd

def read_csv():
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("./data/auto-mpg.data", header=None, names=names, delim_whitespace=True)
    return df

# Remving outliers from the data
def outlier_detection(df):
    df = df.quantile([.90, .10])
    return df

print(outlier_detection(read_csv()))