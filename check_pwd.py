import re

def check_pwd(pwd):
    # validate length
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    
    # check for a lowercase letter
    lower_case = re.search('[a-z]', pwd)
    if lower_case is None:
        return False
    
    return True