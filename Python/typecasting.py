# Type casting example in Python

# Ask the user for a string that represents a number
number_input = input("Enter a number (integer or decimal): ")

# Convert the string to an integer
try:
    integer_number = int(number_input)
    print(f"The number {number_input} as an integer is: {integer_number}")
except ValueError:
    print(f"Cannot convert {number_input} to an integer.")

# Convert the string to a float
try:
    float_number = float(number_input)
    print(f"The number {number_input} as a float is: {float_number}")
except ValueError:
    print(f"Cannot convert {number_input} to a float.")

# Convert the integer to a string (using the float conversion to avoid exceptions)
string_number = str(float_number)
print(f"The number {float_number} as a string is: {string_number}")

# Display boolean representation of the float
boolean_value = bool(float_number)
print(f"The boolean value of {float_number} is: {boolean_value}")
