'''
Simple Interest Calculator (SIC)
It calculates simple interest based on user input.
'''

print("Welcome to SIC!")

# Get user inputs
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100
total = principal + simple_interest

# Display the result
print(f"The simple interest is: {simple_interest}")
print(f"Principal + Simple Interest = {total}")
