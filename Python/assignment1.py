# Variables and Data Types
integer_var = 42
float_var = 3.14159
string_var = "Hello, Python!"
boolean_var = True
list_var = [1, 2, 3, 4, 5]

print(f"Integer: {integer_var}, Type: {type(integer_var)}")
print(f"Float: {float_var}, Type: {type(float_var)}")
print(f"String: {string_var}, Type: {type(string_var)}")
print(f"Boolean: {boolean_var}, Type: {type(boolean_var)}")
print(f"List: {list_var}, Type: {type(list_var)}\n")

# For Loop to Print Numbers 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)
print("\n")

# Even or Odd Checker
number = int(input("Enter an integer to check if it is even or odd: "))
if number % 2 == 0:
    print("The number is even.\n")
else:
    print("The number is odd.\n")

# Casting from String to Integer and Float
num_str = input("Enter a number (integer expected): ")
num_int = int(num_str)
print(f"Converted Integer: {num_int}, Type: {type(num_int)}\n")

num_str_float = input("Enter another number for float conversion: ")
num_float = float(num_str_float)
print(f"Converted Float: {num_float}, Type: {type(num_float)}\n")

# Match case menu driven program
def perform_operation(num1, num2, choice):
    match choice:
        case "1":
            return num1 + num2
        case "2":
            return num1 - num2
        case "3":
            return num1 * num2
        case "4":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        case _:
            return "Invalid operation"

first_num = float(input("Enter the first number for operations: "))
second_num = float(input("Enter the second number for operations: "))
print("Choose the operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
operation = input("Enter choice (1/2/3/4): ")

result = perform_operation(first_num, second_num, operation)
print(f"Result: {result}")
