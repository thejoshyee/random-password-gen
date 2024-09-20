# main.py
# The main module that the password generator will run the program from.

from password_flow import generate_password_flow


def main():
  """Main function to run the password generator program."""
  print(
      "Hello there friend! This password generator is ready to serve you" 
      " with the most complex and secure password!"
  )
  generate_password_flow()  # Start the password generating process


main()
