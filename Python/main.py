# This is a comment - it explains what the code does

# Variables and Data Types
number = 10               # Integer
pi = 3.14159              # Floating point number
greeting = "Hello, Python!" # String
is_active = True          # Boolean

# Basic Operations
sum = number + 5
difference = number - 5
product = number * 2
quotient = number / 2

# Print function to output results
print(greeting)
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# Conditional Statements
if number > 5:
    print("Number is greater than 5")
elif number == 5:
    print("Number is exactly 5")
else:
    print("Number is less than 5")

# Loop: for loop that prints numbers 0 through 4
for i in range(5):
    print(i)

# While loop example
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Function definition and calling it
def square(x):
    return x * x

print("Square of number:", square(number))
