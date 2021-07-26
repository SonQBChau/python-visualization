from collections import Counter
marriage_ages = [22, 22, 25, 25, 30, 24, 26, 24, 35]  # create a list
value_counts = Counter(marriage_ages)  # apply the counter functionality
print(value_counts.most_common())

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