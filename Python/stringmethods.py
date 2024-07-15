def demonstrate_string_methods():
    sample_text = "Hello, world!"

    # Upper and lower case methods
    print("Upper case:", sample_text.upper())
    print("Lower case:", sample_text.lower())

    # Strip method
    padded_text = "   space around   "
    print("Stripped text:", padded_text.strip())

    # Find and replace methods
    print("Position of 'world':", sample_text.find('world'))
    print("Replace 'world' with 'Python':", sample_text.replace('world', 'Python'))

    # Split method
    print("Split by comma:", sample_text.split(','))

    # Length of string
    print("Length of the text:", len(sample_text))

if __name__ == "__main__":
    demonstrate_string_methods()
