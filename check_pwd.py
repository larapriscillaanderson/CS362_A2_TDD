import re

def check_pwd(pwd):
    # validate length
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    
    # check for a lowercase letter
    lower_case = re.search('[a-z]', pwd)
    if lower_case is None:
        return False
    
    # check for a uppercase letter
    upper_case = re.search('[A-Z]', pwd)
    if upper_case is None:
        return False
    
    # check that there is at least one digit
    digit = re.search('[0-9]', pwd)
    if digit is None:
        return False
    
    return True