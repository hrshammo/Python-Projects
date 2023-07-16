import string
from itertools import product
import random


def generate_password_option():
    while True:
        length = int(input("Enter the length of the password: "))
        print("---------------------------------------")
        print("Enter the options you want in your password: ")
        print("---------------------------------------")
        print("1. Big Alphabets")
        print("2. Small Alphabets")
        print("3. Special Characters")
        print("4. Numbers")

        options = input("Enter the options for the password (comma-separated - 1,2,4): ")

        password = generate_password(length, options.split(","))
        print("Generated Password:", password)
        print("---------------------------------------")
        strength = check_strength(password.lower())
        print("Password strength:", strength)
        print("---------------------------------------")

        reload = input("Do you want to generate another password? (yes/no): ")
        if reload.lower() != "yes":
            break
def generate_password(length, options):
    characters = ""
    if "1" in options:
        characters += string.ascii_uppercase
    if "2" in options:
        characters += string.ascii_lowercase
    if "3" in options:
        characters += string.punctuation
    if "4" in options:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_special = any(char in string.punctuation for char in password)
    has_number = any(char.isdigit() for char in password)

    if length < 8 or (length < 8 and not (has_uppercase and has_lowercase and has_special and has_number)):
        return "Weak"
    elif length < 12 or (length < 12 and not (has_uppercase and has_lowercase and has_special and has_number)):
        return "Moderate"
    else:
        return "Strong"

def check_strength_option():
    while True:
        password = input("Enter the password to check its strength: ")
        strength = check_strength(password)
        print("Password strength:", strength)
        print("---------------------------------------")

        reload = input("Do you want to check another password? (yes/no): ")
        if reload.lower() != "yes":
            break

def generate_passwords(length_range, options):
    start, end = map(int, length_range.split(","))
    characters = ""
    
    if "1" in options:
        characters += string.ascii_uppercase
    if "2" in options:
        characters += string.ascii_lowercase
    if "3" in options:
        characters += string.punctuation
    if "4" in options:
        characters += string.digits
    
    passwords = []
    for length in range(start, end + 1):
        for password in product(characters, repeat=length):
            passwords.append(''.join(password))
    
    return passwords

def generate_passwords_for_payload():
    length_range = input("Enter the length range for the passwords (e.g., 3, 6): ")
    options = input("Enter the options for the passwords (comma-separated - 1,2,3,4): ")
    
    passwords = generate_passwords(length_range, options.split(","))
    
    with open("passwords.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")
    
    print("Passwords saved to passwords.txt")

def main():
    while True:
        print("-------------------------------------------")
        print("- Password Generator and Strength Checker -")
        print("-------------------------------------------")
        print("- Choice an Options:                      -")
        print("- 1. Check Password Strength              -")
        print("- 2. Generate Password                    -")
        print("- 3. Generate Passwords for Payload       -")
        print("-------------------------------------------")
        option = input("Select an option (1, 2, or 3): ")
        print("---------------------------------------")

        if option == "3":
            generate_passwords_for_payload()
            break
        elif option == "1":
            check_strength_option()
        elif option == "2":
            generate_password_option()

        reload = input("Do you want to perform another operation? (yes/no): ")
        if reload.lower() != "yes":
            break

if __name__ == "__main__":
    main()
