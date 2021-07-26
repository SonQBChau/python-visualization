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

##################
# SETS IN PYTHON #
##################
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(1)
# Note that the set only contains a single 1 value
print("---0---")
print(my_set)

my_set2 = set()
my_set2.add(1)
my_set2.add(2)
my_set2.add(3)
my_set2.add(4)
print("---1---")
print(my_set2)

# Prints the overlap
print("---1---")
print(my_set.intersection(my_set2))
print("---2---")

# Prints the combination
print(my_set.union(my_set2))

# Prints the difference (those in my_set but not my_set2)
print("---3---")
print(my_set.difference(my_set2))

#########################
# THE IF-ELSE CONSTRUCT #
#########################
def age_check(age):

    if age > 40:  # if age greater than 40, print "Older than 40"
        print("Older than 40")
    elif age > 30 and age <= 40: # if age greater than 30 and less than or equal to 40, print "Between 30 and 40"
        print("Between 30 and 40")
    else:  # if neither of the previous conditions are met, print "Other"
        print("Other")

print(age_check(41))

#####################
# THE FOR CONSTRUCT #
#####################
names = ['tyler', 'karen', 'jill']   # list containing names

for i, name in enumerate(names):     # iterating over names
    print("Index: {0}".format(i))    # printing index number
    print("Value: {0}".format(name)) # print the value at the index

# list comprehensions
numbers_gt_5 = [x for x in range(1,15) if x > 5]  # loop over the range and only keep the value if greater than 5
print(numbers_gt_5)

nums_plus_one = [x + 1 for x in range(5)] # increment every value in a list by 1
print(nums_plus_one)

#####################
# THE SORT FUNCTION #
#####################
my_list = [2, 10, 1, -5, 22]
my_list.sort()  # sorting the list

print(my_list)

my_list = [2, 10, 1, -5, 22]

# Sorted reversely on basis of absolute value
my_list_sorted_abs = sorted(my_list, key=abs, reverse=True)

print(my_list_sorted_abs)

####################
# THE ZIP FUNCTION #
####################
list_1 = [1, 2, 3]  # create your first list
list_2 = ['x', 'y', 'z']  # create your second list

print(list(zip(list_1, list_2)))  # combine and print

pairs = [('x', 1), ('y', 2), ('z', 3)]  # a list of tuples
letters, numbers = zip(*pairs)  # break into two lists

print(letters)  # print the first values of the tuples
print(numbers)  # print the second values of the tuples