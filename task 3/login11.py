import input_helpers

user_data = {}  # Dictionary to store user data


def read_user_data(file_path):
    """
    Read user data from a file and store it in a dictionary.

    Args:
        file_path (str): Path to the file containing user information.

    Prints:
        Error messages for file not found, permission issues, or other exceptions.
    """
    try:
        with open(file_path, "r") as file:
            for line in file:
                user, _, password = line.strip().split(":")
                user_data[user] = {'password': password}
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def login_user(login_username, hashed_password):
    """
    Validates user credentials against the user data dictionary.

    Args:
        login_username (str): User-entered username for login.
        hashed_password (str): Hashed password for login.

    Prints:
        "Access granted" if login is successful, otherwise "Access denied".
        Error message if an exception occurs during the validation process.
    """
    try:
        if login_username in user_data and user_data[login_username]['password'] == hashed_password:
            print("Access granted")
        else:
            print("Access denied")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to handle user login.
    """
    try:
        file_path = "passwd.txt"
        # Read user data from the file
        read_user_data(file_path)

        # Get the username and password from the user
        login_username = input_helpers.non_empty_input("Enter username: ")
        login_password = input_helpers.secure_input("Enter password: ")
        hashed_password = input_helpers.encrypt(login_password)

        # Call the login_user function to validate the user credentials
        login_user(login_username, hashed_password)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
