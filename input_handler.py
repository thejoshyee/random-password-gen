# input_handler.py
# This module handles user input and validation.


def get_password_length():
  """Prompt user for password length ensuring it is between 12 and 64."""
  while True:
    try:
      length = int(input("Enter the password length (12 to 64 characters): "))
      if 12 <= length <= 64:
        return length
      else:
        print("Password length must be between 12 and 64 characters.")
    except ValueError:
      print("Invalid input. Please enter a number.")


def get_special_characters_selection():
  """Ask user if they want to include special characters in the password."""
  while True:
    choice = input("Include special characters (yes/no)? ").strip().lower()
    if choice in ['yes', 'no']:
      return choice == 'yes'
    print("Please enter 'yes' or 'no'.")


def generate_additional_password():
  """Ask the user if they want to generate another password."""
  while True:
    choice = input(
      "Do you want to generate another password? (yes/no): ").strip().lower()
    if choice in ['yes', 'no']:
      return choice == 'yes'
    print("Please tell me if you want to generate another password or not. I don't have all day!")
