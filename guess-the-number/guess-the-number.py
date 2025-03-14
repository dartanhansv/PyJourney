import random

"""
Guessing the Number Game!
The user guesses a random number
"""

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("I have picked a number between 1 and 10. Can you guess it?")

# Ask the user to guess and check if he got it right

while True:
    guess = int(input("Enter your guess: "))
    if guess == random_number:
        print("Awesome! You guess it!")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
