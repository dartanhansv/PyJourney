"""
In Python (and many other programming languages), -1 often has a special meaning, especially when working with
functions or methods that return indices or positions:

In string methods like find() or index(), -1 is typically used to indicate that a substring was not found. Example:

address = "That is not an email address"
at = address.find("@")

In this case, since there is no period (dot) in the string, text.find(".") will return -1
"""


def addressVal(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("Invalid")
    elif (at == -1):
        print("Invalid")
    else:
        print("Valid")


print("This program will decide if your input is a valid email address")
while True:
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address:")

    addressVal(x)
