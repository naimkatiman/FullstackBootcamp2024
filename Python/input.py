def get_input():
    """Prompt the user for two numbers and return them."""
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def calculate_sum(a, b):
    """Calculate and return the sum of two numbers."""
    return a + b

def main():
    # Get user input
    num1, num2 = get_input()
    
    # Calculate the sum of the inputs
    result = calculate_sum(num1, num2)
    
    # Display the result
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
