import input_helpers

user_data = {}  # Dictionary to store user data


def is_duplicate_user(user):
    """
    Check if a given username already exists in the user data.

    Parameters:
    - user (str): The username to check.

    Returns:
    - bool: True if the username already exists, False otherwise.
    """
    if user in user_data:
        return True
    return False


def add_user_to_data(user, real_name, hashed_password):
    """
    Add a new user to the user data dictionary.

    Parameters:
    - user (str): The username of the new user.
    - real_name (str): The real name of the new user.
    - hashed_password (str): The hashed password of the new user.
    """
    try:
        with open("passwd.txt", "a") as file:
            file.write(f"{user}:{real_name}:{hashed_password}\n")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")


def main():
    """
    Main function to execute user creation process.

    This function prompts the user to enter a unique username, a real name, and a password. It then encrypts the password
    and adds the user's information to the user_data dictionary if the username is not already taken. If any error occurs
    during the process, it prints an error message.

    Returns:
        None
    """
    try:
        while True:
            # Get a non-empty username from the user
            user = input_helpers.non_empty_input("Enter username: ")

            # Check if the username already exists
            if is_duplicate_user(user):
                print("Username already exists. Please choose a different username.")
            else:
                break  # Break out of the loop if the username is not a duplicate

        # Get the real name from the user
        real_name = input_helpers.non_empty_input("Enter real name: ")
        # Get a secure password from the user
        password = input_helpers.secure_input("Enter password: ")
        # Encrypt the password
        hashed_password = input_helpers.encrypt(password)

        # Add the new user to the data
        add_user_to_data(user, real_name, hashed_password)
        print("User created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
