import random
import string

def generate_password(length, complexity):
    """Generates a random password of the specified length and complexity."""
    characters = string.ascii_letters + string.digits + string.punctuation

    if complexity == 'simple':
        characters = string.ascii_letters + string.digits
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    """Prompts the user for input and generates a password."""
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length must be at least 4 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    complexity = input("Enter the desired complexity (simple or strong): ")

    password = generate_password(length, complexity)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
