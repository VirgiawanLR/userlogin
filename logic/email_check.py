import re

# Define a function for
# for validating an Email
def check(email):
    # Make a regular expression
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	# pass the regular expression
	# and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
