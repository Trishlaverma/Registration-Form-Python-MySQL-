import re
def valid_password(PASSWORD):

# check length
    if len(PASSWORD) < 8 or len(PASSWORD) > 12:
        return False
# Check for at least one capital letter
    if not re.search(r'[A-Z]', PASSWORD):
        return False
# Check for at least one digit
    if not re.search(r'[0-9]', PASSWORD):
        return False
# Check for at least one special character
    if not re.search(r'[!@#$%^&*?]', PASSWORD):
        return False
    
    return True

