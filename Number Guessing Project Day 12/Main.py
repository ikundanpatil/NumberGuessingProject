from Art import logo
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

# Functions to check user's guess against actual answer.

def check(user_guess, actual_result, attempts):

    """Checks Answer against guess, return the number of attempts remaining"""

    if user_guess < actual_result:
        print("Too low")
        return attempts - 1
    elif user_guess > actual_result:
        print("Too High")
        return attempts - 1
    else:
        print(f"You got it! The answer was {actual_result}")


# Function to set difficulty

def defficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_ATTEMPTS
    elif level == "hard":
        return HARD_ATTEMPTS
    else:
        print("You choose a wrong difficulty level.")



def game():

    print(logo)

    # Choosing A random number between 1 to 100.

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    result = randint(1,100)

    print(result)


    attempts = defficulty_level()

    guess = 0

    while guess != result:
        print(f"You have {attempts} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess: "))
        attempts = check(guess, result, attempts)

        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return
        elif guess != attempts:
            print("Guess again.")
            
game()
