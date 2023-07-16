 
# Password Generator and Strength Checker
This project is a Python script that provides functionality for generating passwords and checking their strength. It offers a command-line interface for users to interact with.

## How to Use
Clone or download the repository from GitHub.
Ensure that you have Python installed on your system.
Open a terminal or command prompt and navigate to the project directory.
Run the script by executing the following command: python password_generator.py.
Follow the on-screen instructions to perform the desired operations.  <br>

![image](https://github.com/hrshammo/Python/assets/76872754/2252ee1f-8ff9-4e55-9964-a5945a8205a3)

## Features
### 1. Check Password Strength
This option allows you to check the strength of a given password. It analyzes the password based on the following criteria:

Length: The length of the password must be at least 8 characters for a "Weak" rating, 12 characters for a "Moderate" rating, and greater than 12 characters for a "Strong" rating.
Character Types: The password must contain a combination of uppercase letters, lowercase letters, special characters, and numbers.
 <br>
![image](https://github.com/hrshammo/Python/assets/76872754/aa6f1d27-e594-4d32-a2bc-4a038620fcb6)

### 2. Generate Password
This option lets you generate a random password with customizable options. You can specify the desired password length and choose from the following options:

Big Alphabets (uppercase letters)
Small Alphabets (lowercase letters)
Special Characters
Numbers
The generated password will be displayed, along with its strength rating.
 <br>
 
![image](https://github.com/hrshammo/Python/assets/76872754/7ab6bb37-418c-4fe7-aaea-b28e656b835f)

### 3. Generate Passwords for Payload
This option generates a list of passwords within a specified length range. You can define the range (e.g., 3 to 6) and select the desired password options. The passwords will be saved to a file named "passwords.txt" in the project directory.
 <br>
![image](https://github.com/hrshammo/Python/assets/76872754/2a0251b5-f80e-4a88-8cc4-7baecf924de3)
![image](https://github.com/hrshammo/Python/assets/76872754/80e83bfd-71da-48ee-9fab-c581374f71bd)  <br>
![image](https://github.com/hrshammo/Python/assets/76872754/4e88f071-96e4-45d4-8b3b-54c003362e07)


Please note that the generated passwords should be used responsibly and in accordance with security best practices. It is recommended to store passwords securely and avoid sharing them or using them for sensitive accounts.

## Dependencies

The script requires Python 3 and utilizes the following modules:

- `string`: Provides a collection of commonly used string constants.
- `itertools.product`: Generates the Cartesian product of input iterables.
- `random`: Generates random numbers and makes use of the random.choice() function.
- `sys`: Provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter.

To ensure the required dependencies are available, you can run the following command: `pip install -r requirements.txt`.

## Contributions
Contributions to this project are welcome. If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to submit a pull request on GitHub.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for personal or commercial purposes.
