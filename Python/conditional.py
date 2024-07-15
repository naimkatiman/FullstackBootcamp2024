def check_number():
    num = int(input("Enter a number: "))
    if num > 0:
        print(f"{num} is positive.")
    elif num == 0:
        print(f"{num} is zero.")
    else:
        print(f"{num} is negative.")

def compare_numbers():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a > b:
        print(f"{a} is greater than {b}.")
    elif a < b:
        print(f"{a} is less than {b}.")
    else:
        print(f"{a} is equal to {b}.")

def grade_evaluation():
    score = int(input("Enter your score: "))
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

if __name__ == "__main__":
    print("Number Check")
    check_number()

    print("\nNumber Comparison")
    compare_numbers()

    print("\nGrade Evaluation")
    grade_evaluation()
