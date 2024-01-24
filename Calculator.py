def calculator():
    """Performs basic arithmetic operations based on user input."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
        print(num1, "+", num2, "=", result)
    elif choice == 2:
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif choice == 3:
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif choice == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print(num1, "/", num2, "=", result)

if __name__ == "__main__":
    calculator()
