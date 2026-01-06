import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of number between 1 and 100.")
EASY_LEVEL = 10
HARD_LEVEL = 5
number = random.randint(1, 100)


def check_answer(number, guess):
    if guess == number:
        print(f"You guessed it Correctly! the answer was {number}")
        return True
    elif guess>number:
        print("Too high")
        return False
    else:
        print("Too low")
        return False

def set_diffuclty():
    difficulty = input("Choose Difficulty: Type 'easy' or 'hard':\n")
    if difficulty.lower() == "hard":
        return HARD_LEVEL
    elif difficulty.lower()=="easy":
        return EASY_LEVEL


def game():
    attempts = set_diffuclty()
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\t"))
        if check_answer(number,guess):
            return
        attempts -= 1
    else:
        print("You run out of guesses, you lose.")
        print(f"The Number was {number}")


game()