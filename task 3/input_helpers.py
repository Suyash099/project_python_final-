import getpass
import hashlib

def non_empty_input(prompt):
    """
    Prompt the user for input until a non-empty string is provided.

    Parameters:
    - prompt (str): The prompt message to display.

    Returns:
    - str: The non-empty input provided by the user.
    """
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("Input cannot be empty. Please try again.")


def secure_input(prompt):
    """
    Prompt the user for input without showing it on the screen.

    Parameters:
    - prompt (str): The prompt message to display.

    Returns:
    - str: The hashed input provided by the user.
    """
    while True:
        password = getpass.getpass(prompt)
        if password.strip():
            # Hash the password using hashlib
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            # Concatenate "***" to the hashed password
            return hashed_password + "***"
        else:
            print("Password cannot be empty. Please try again.")

def encrypt(password):
    """
    Encrypts a password using SHA-256 hashing.

    Parameters:
    - password (str): The password to encrypt.

    Returns:
    - str: The hashed password.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def read_file(file_path):
    """
    Reads the content of a file.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - list: A list containing the lines of the file.
    """
    with open(file_path, "r") as file:
        return file.readlines()
    
def write_file(file_path, lines):
    """
    Writes lines to a file.

    Parameters:
    - file_path (str): The path to the file.
    - lines (list): A list of lines to write to the file.
    """
    with open(file_path, "w") as file:
        file.writelines(lines)


