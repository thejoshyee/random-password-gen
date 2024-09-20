# password_flow.py
# Module to handle the interactive flow of generating the passwords.

from input_handler import (
    generate_additional_password,
    get_password_length,
    get_special_characters_selection,
)
from password_generator import generate_character_set, generate_password


def generate_password_flow():
    """Handles the interactive process of generating passwords."""
    length = get_password_length()
    include_special_chars = get_special_characters_selection()
    characters = generate_character_set(include_special_chars)
    password = generate_password(length, characters)
    print("Your new password is:", password)

    if generate_additional_password():
        generate_password_flow()
    else:
        print("Goodbye! Thank you for using our password generator."
              " See you again soon!")
