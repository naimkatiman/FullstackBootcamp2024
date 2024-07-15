def check_access(age, member_status):
    if age > 18:
        if member_status.lower() == "yes":
            print("Access granted: Welcome to the club!")
        else:
            print("Access denied: Membership is required for entry.")
    else:
        print("Access denied: You must be over 18 years old.")

def vacation_plan(budget, destination):
    if budget > 1000:
        if destination == "beach":
            print("You can plan a luxurious beach vacation in Maldives.")
        elif destination == "mountain":
            print("You can plan a hiking trip in the Swiss Alps.")
        else:
            print("You can plan a city tour in Paris.")
    elif budget > 500:
        if destination == "beach":
            print("Consider a trip to Florida's beaches.")
        elif destination == "mountain":
            print("Consider a trip to Colorado's mountains.")
        else:
            print("Consider a trip to Las Vegas.")
    else:
        print("Consider staying local and exploring nearby attractions.")

if __name__ == "__main__":
    print("Access Check")
    check_access(20, "yes")
    check_access(20, "no")
    check_access(17, "yes")

    print("\nVacation Planning")
    vacation_plan(1200, "beach")
    vacation_plan(800, "mountain")
    vacation_plan(400, "city")
