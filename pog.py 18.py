#Write a Python function to insert a string in the middle of a string
string = "Hello world"
insert_string = " beautiful"

# Get the length of the original string
length = len(string)

# Get the index where we want to insert the new string
middle_index = length // 2

# Use slicing to split the original string in half and insert the new string in between
result = string[:middle_index] + insert_string + string[middle_index:]

print(result)
