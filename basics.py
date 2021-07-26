from collections import Counter
marriage_ages = [22, 22, 25, 25, 30, 24, 26, 24, 35]  # create a list
value_counts = Counter(marriage_ages)  # apply the counter functionality
print(value_counts.most_common())