import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    print("You have 5 chances to guess the correct number.\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < number_to_guess:
            print("The number is greater than your guess.\n")
        elif guess > number_to_guess:
            print("The number is less than your guess.\n")
        else:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempt} attempts!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")

if __name__ == "__main__":
    guessing_game()
