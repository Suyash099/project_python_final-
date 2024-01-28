import input_helpers

user_data = {}  # Dictionary to store user data


def read_user_data(file_path):
    """
    Read user data from a file and store it in a dictionary.

    Args:
        file_path (str): Path to the file containing user information.
    """
    try:
        with open(file_path, "r") as file:
            for line in file:
                user, real_name, password = line.strip().split(":")
                user_data[user] = {'real_name': real_name, 'password': password}
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_user_data(file_path):
    """
    Write user data from the dictionary to a file.

    Args:
        file_path (str): Path to the file to write user information.
    """
    try:
        with open(file_path, "w") as file:
            for user, data in user_data.items():
                file.write(f"{user}:{data['real_name']}:{data['password']}\n")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission issue while accessing the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def change_password(changed_user, hashed_password):
    """
    Change the password for a specified user in the user data dictionary.

    Args:
        changed_user (str): The user for whom the password needs to be changed.
        hashed_password (str): The hashed current password for verification.
    """
    try:
        # Check if the user exists and the password matches
        if changed_user in user_data and user_data[changed_user]['password'] == hashed_password:
            new_password = input_helpers.secure_input("Enter the new password: ")
            confirm_password = input_helpers.secure_input("Confirm the new password: ")

            if new_password == confirm_password:
                # Update the password in the user data dictionary
                user_data[changed_user]['password'] = input_helpers.encrypt(new_password)
                return True
            else:
                print("Passwords do not match. Password change aborted.")
                return False
        else:
            print(f"User '{changed_user}' not found or password does not match. Password change aborted.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main():
    """
    Main function to initiate the process of changing a user's password.
    """
    try:
        # Path to the file containing user information
        file_path = "passwd.txt"
        # Read user data from the file
        read_user_data(file_path)

        # Get the username of the user whose password needs to be changed
        changed_user = input_helpers.non_empty_input("Enter the user to be changed: ")
        # Get the current password of the user
        changed_password = input_helpers.secure_input("Enter the current password: ")

        # Encrypt the current password
        hashed_password = input_helpers.encrypt(changed_password)

        # Change the password for the specified user
        if change_password(changed_user, hashed_password):
            # Write updated user data back to the file
            write_user_data(file_path)
            print(f"Password for user '{changed_user}' has been successfully changed.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
