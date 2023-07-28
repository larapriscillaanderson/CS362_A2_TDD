def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    
    return True