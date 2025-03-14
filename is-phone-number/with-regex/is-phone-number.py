'''
This is an example of pattern matiching with using regular expressions
'''

import re

# Create a regex pattern to search for US phone number format: xxx-xxx-xxxx
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Strings to check
input_var1, input_var2 = '212-555-6789', '1 91234-5678'

# search for the pattern
isphoneNumber1 = phoneNumberRegex.search(input_var1)
isphoneNumber2 = phoneNumberRegex.search(input_var2)

# test it
if isphoneNumber1:
    print(f"{isphoneNumber1.group()} is a US phone number")
elif isphoneNumber2:
    print(f"{isphoneNumber2.group()} is a US phone number")
else:
    print("No US phone number found")

