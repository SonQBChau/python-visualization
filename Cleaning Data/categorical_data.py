import pandas as pd

# Create series with male and female values
non_categorical_series = pd.Series(['male', 'female', 'male', 'female'])
print(non_categorical_series)

##################
# LABEL ENCODING #
##################
# Convert the text series to a categorical series
categorical_series = non_categorical_series.astype('category')
# Print the numeric codes for each value
print(categorical_series.cat.codes)
# Print the category names
print(categorical_series.cat.categories)

####################
# ONE-HOT ENCODING #
####################
# Create dummy or one-hot encoded variables
print(pd.get_dummies(non_categorical_series))