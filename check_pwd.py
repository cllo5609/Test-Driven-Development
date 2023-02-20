# Author     : Clinton Lohr
# Date       : 02/17/2023
# Course     : CS 362 - Software Engineering II
# Assignment : TDD Hands On

# Function for checking if a password is valid
def check_pwd(input_str):

    lower_check = False
    upper_check = False
    digit_check = False
    special_check = False
    special_chars = "~`!@#$%^&*()_+-="

    # Checks if the length of the entered password is between 8 and 20 characters (inclusive)
    if len(input_str) < 8 or len(input_str) > 20:
        return False

    # Checks if the input string contains at least one lowercase letter
    for i in input_str:
        if i.islower():
            lower_check = True
            break

    # Checks if the input string contains at least one uppercase letter
    for i in input_str:
        if i.isupper():
            upper_check = True
            break

    # Checks if the input string contains at least one digit
    for i in input_str:
        if i.isdigit():
            digit_check = True
            break

    # Checks if the input string contains at least one valid special character
    for i in input_str:
        if i in special_chars:
            special_check = True
            break

    # Checks if all criteria for a valid password was met
    if upper_check and lower_check and digit_check and special_check:
        return True

    return False
