# number_guessing_game.py
# A simple number guessing game (1–10)

import random


def main():
    # Step 1: Generate a random number
    secret_number = random.randint(1, 10)

    # Step 2: Display welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    # Step 3: Ask user for their first guess
    guess = int(input("Enter your guess: "))

    # Step 4: Repeat until the correct number is guessed
    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        guess = int(input("Enter your new guess: "))

    # Step 5: Correct guess
    print("🎉 Congratulations! You guessed it right.")


# Run the game
if __name__ == "__main__":
    main()
