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


def delete_user(deleted_user, hashed_password):
    """
    Deletes a user from the user data dictionary if the provided user and hashed password match.

    Args:
        deleted_user (str): The user to be deleted.
        hashed_password (str): The hashed password for verification.

    Returns:
        bool: True if the user was successfully deleted, False otherwise.
    """
    try:
        if deleted_user in user_data and user_data[deleted_user]['password'] == hashed_password:
            del user_data[deleted_user]
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main():
    """
    Main function to execute user deletion process.
    """
    try:
        # Path to the file containing user information
        file_path = "passwd.txt"
        # Read user data from the file
        read_user_data(file_path)

        # Get the user to be deleted and their password
        deleted_user = input_helpers.non_empty_input("Enter the user to be deleted: ")
        deleted_password = input_helpers.secure_input("Enter the password: ")

        # Encrypt the provided password
        hashed_password = input_helpers.encrypt(deleted_password)

        # Attempt to delete the user
        if delete_user(deleted_user, hashed_password):
            # Write updated user data back to the file
            write_user_data(file_path)
            print(f"User '{deleted_user}' has been successfully deleted.")
        else:
            print("User deletion failed. Please check the provided username and password.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
