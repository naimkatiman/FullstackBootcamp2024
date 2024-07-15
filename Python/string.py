# Creating a string
my_string = "Hello, World!"

# Accessing characters in a string
first_char = my_string[0]  # 'H'
last_char = my_string[-1]  # '!'

# Slicing a string
substring = my_string[1:5]  # 'ello'

# Concatenating strings
greeting = my_string + " How are you?"

# Formatting strings (using f-string for Python 3.6+)
name = "Alice"
personalized_greeting = f"{name}, {my_string.lower()}"

# Replacing parts of a string
modified_string = my_string.replace("World", "Python")

# Checking if a string contains a substring
contains_hello = "Hello" in my_string  # True

# Printing results
print("First character:", first_char)
print("Last character:", last_char)
print("Substring:", substring)
print("Concatenated string:", greeting)
print("Personalized greeting:", personalized_greeting)
print("Modified string:", modified_string)
print("Contains 'Hello':", contains_hello)
