'''
This is an example of pattern matiching with using regular expressions
'''

import re

# Create a regex pattern to search for US phone number format: xxx-xxx-xxxx
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# String to check
data = "Any random text where phone number such as 111-222-3333 or 123-456-7890 can be found."

# search for the pattern
PhoneFound = phoneNumberRegex.findall(data)

# Print result
if PhoneFound:
    for phone in PhoneFound:
        print(f"Phone number found: {phone}")
        found_number = True
else:
    print("Could not find any phone numbers")
