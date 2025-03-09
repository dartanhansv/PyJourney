'''
A calculator that performs basic arithmetic operations
'''

# Greating
print("\n Welcome to the Basic_Calc!\n")

# Get numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operation
print("\nChoose an arithmetic operation: (+), (-), (*), or (/)")
operation = input("Enter the operation: ")
print("\n")

# Perform the calculation
if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed!")

else:
    print("Invalid operation")

print(f"The result is: {result}")