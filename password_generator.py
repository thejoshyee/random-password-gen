# password_generator.py
# This module generates the password based on provided specs.
import random
import string


def generate_character_set(include_special_chars):
  """Generate a set of characters that may include special characters."""
  characters = string.ascii_letters + string.digits
  if include_special_chars:
    characters += string.punctuation
  return characters

def generate_password(length, characters):
  """Generate a random password of the specified length using the provided characters."""
  return ''.join(random.choice(characters) for _ in range(length))
