# Lists are mutable and cannot be used directly as dictionary keys
my_list = [1, 2, 3]
my_dict = {tuple(my_list): "List converted to tuple as a key"}
print(my_dict[tuple(my_list)])  # Output: List converted to tuple as a key

# Modify the list
my_list.append(4)

# Update the dictionary 
my_dict[tuple(my_list)] = "Updated key with new element"
print(my_dict)

print(my_dict[tuple(my_list)])  # Output: Updated key with new element
