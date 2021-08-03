import tempfile

tmp = tempfile.NamedTemporaryFile()

# Open the file for writing. And write the data.
# with open(tmp.name, 'w') as f:
#     f.write("James|22|M\n")
#     f.write("Sarah|31|F\n")
#     f.write("Mindy|25|F")

# Read in the data from our file, line by line
# with open(tmp.name, "r") as f:
with open('tmp.name', "r") as f:
    for line in f:
      print(line)
      
      
first_values = []  # Define a list to store the first values of each row
with open('tmp.name', "r") as f:  # Open the file to read
    for line in f:  # Loop over each line
      row_values = line.split("|")  # Split each line by the | character into a list
      first_values.append(row_values[0])  # Add the first value to our list
      
print(first_values)