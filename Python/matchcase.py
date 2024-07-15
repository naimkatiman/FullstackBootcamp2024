# Prompt the user for input
user_input = input("Enter a color (red, blue, green): ")

# Using match-case to respond based on the input
match user_input.lower():  # Convert to lowercase to handle case insensitivity
    case "red":
        print("You chose red! It's a warm color.")
    case "blue":
        print("You chose blue! It's a cool and calming color.")
    case "green":
        print("You chose green! It symbolizes nature and growth.")
    case _:
        print("That's not a color option I recognize.")

# This code will print different messages based on the color entered by the user.
