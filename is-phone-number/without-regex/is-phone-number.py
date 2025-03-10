'''
This is an example of pattern matiching without using regular expressions
'''

def isPhoneNumber(input_var): # check if it a phone number in US format: "AreaCode-ExcahngeCode-SubscriberNumber" = xxx-xxx-xxxx
    # check if it is 12 characters long
    if len(input_var) != 12: 
        # if it is not 12 char long, it is not phone number-sized
        return False
    
    # check if the first 3 digits are deciaml, like an area code would 
    for digit in range(0, 3): 
        if not input_var[digit].isdecimal():
            # if missing the 1st dash, return false
            return False 

    # check if the 4th digit (index 3) is dash    
    if input_var[3] != '-': 
        return False
    
    # repeat the decimal check for the next 3 digits
    for digit in range(4, 7): 
        if not input_var[digit].isdecimal():
            return False
        
    # check if the 8th digit (index 7) is dash
    if input_var[7] != '-':
        # if missing the 2nd dash, return false
        return False

     # repeat the decimal check for last 4 digits
    for digit in range(8, 12): 
        if not input_var[digit].isdecimal():
            return False

    return True


# Test it with a valid phone number
input_var = '212-555-6789'
print(f'Checking if ("{input_var}") is a Phone Number...')
print(isPhoneNumber(input_var))

# Test it with a not valid phone number
input_var = 'That is not a phone number'
print(f'Checking if ("{input_var}") is a Phone Number...')
print(isPhoneNumber(input_var))


