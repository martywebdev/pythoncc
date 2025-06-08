def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.lower() == 'q':
            print("Exiting...")
            break
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def main():
    number1 = get_valid_number("Enter a number (or 'q' to quit): ")
    number2 = get_valid_number("Enter another number (or 'q' to quit): ")

    result = number1 + number2
    print(f"The result of adding {number1} and {number2} is {result}.")

if __name__ == "__main__":
    main()
