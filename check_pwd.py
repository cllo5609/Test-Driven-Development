def check_pwd(input_str):
    lower_check = False
    upper_check = False
    digit_check = False
    special_check = False
    special_chars = "~`!@#$%^&*()_+-="
    if len(input_str) < 8 or len(input_str) > 20:
        return False

    for i in input_str:
        if i.islower():
            lower_check = True
            break

    for i in input_str:
        if i.isupper():
            upper_check = True
            break

    for i in input_str:
        if i.isdigit():
            digit_check = True
            break

    for i in input_str:
        if i in special_chars:
            special_check = True
            break

    if upper_check and lower_check and digit_check and special_check:
        return True

    return False
