def check_pwd(input_str):
    if len(input_str) < 8 or len(input_str) > 20:
        return False
    return True
