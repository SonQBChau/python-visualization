import pandas as pd

def read_csv():
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("./data/auto-mpg.data", header=None, names=names, delim_whitespace=True)
    return df

df = read_csv() 

# Describing data
def group_aggregation(df, group_var, agg_var):
    """
        We need to group the Auto MPG Dataset on the basis of a column. 
        Then we have to calculate the mean of the grouped data according to another column
        
        parameters
            df: A dataframe containing the dataset in the form of a matrix.
            group_var: A variable that will group the data
            agg_var: A variable to aggregate or describe the grouped data with statistics
            
        returns
            dataframe
    """

    # Grouping the data and taking mean
    grouped_df = df.groupby([group_var])[agg_var].mean()
    return grouped_df



# Calling the function
print(group_aggregation(read_csv(),"cylinders","mpg"))