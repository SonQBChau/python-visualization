from collections import Counter
from collections import defaultdict  # import defaultdict class


###########
# COUNTER #
###########
marriage_ages = [22, 22, 25, 25, 30, 24, 26, 24, 35]  # create a list
value_counts = Counter(marriage_ages)  # apply the counter functionality
print(value_counts.most_common())

#######################
# FUNCTIONS IN PYTHON #
#######################
def add_two_numbers(x, y):  # function header
    """
    Takes in two numbers and returns the sum
    parameters
        x : str
            first number
        y : str
            second number
    returns
        x+y
    """
    z = x + y
    return z  # function return
print(add_two_numbers(100,5))  # function  call

y = lambda x, y: x + y  # an anonymous function which takes x and y and input and returns x+y
print(y(100,5))  # call the function anonymous

###################
# LISTS IN PYTHON #
###################
# This creates the list
depths = [1, 5, 3, 6, 4, 7, 10, 12]

# This outputs the first 5 elements. No number before the : implies 0
first_5_depths = depths[:5]

print("---0---")
print(first_5_depths)

# You can easily sum
print("---1---")
print(sum(depths))

# And take the max
print("---2---")
print(max(depths))

# Slicing with a negative starts from the end, so this returns the last element
print("---3---")
print(depths[-1])

# This returns the end of the list starting from the second to the end
# Nothing after the : implies the end of the list
print("---4---")
print(depths[-2:])

# This returns the second, third, and forth elements
# Remember counting starts at zero!
print("---5---")
print(depths[2:5])

##########################
# DICTIONARIES IN PYTHON #
##########################
# Initialize the dictionary.
# Keys are first then a : then the value
my_dict = {"age": 22, "birth_year": 1999, "name": "jack", "siblings": ["jill", "jen"]}

# Get the value for the key age
print("---0---")
print(my_dict['age'])

# Check is age is a key
print("---1---")
print('age' in my_dict)

# Check is company is a key
print("---2---")
print('company' in my_dict)

# Get the value for they key age
print("---3---")
print(my_dict.get('age'))

# Get the value for they key company
# If it doesn't exsist, return 1
print("---4---")
print(my_dict.get('company', 1))

# Return all the keys
print("---5---")
print(my_dict.keys())

# Return all the values
print("---6---")
print(my_dict.values())

# Return all the key, value pairs
print("---7---")
print(my_dict.items())


my_default_dict = defaultdict(int)   # make a default dictionary
my_default_dict['age'] = 22          # adding a key-value pair
print(my_default_dict['company'])    # printing the value of the key "company"

