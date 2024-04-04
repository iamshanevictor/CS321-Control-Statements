import random

hidden_number = random.randint(1, 10)

chances = 3

for i in range(chances):
    guess = int(input(f"Guess the hidden number (Chance {i+1} of {chances}): "))

    if guess == hidden_number:
        print("Congratulations! You guessed the number correctly.")
        break
    else:
        if guess < hidden_number:
            print("Higher")
        else:
            print("Lower")

if guess != hidden_number:
    print(f"Sorry, you didn't guess the number. The hidden number was {hidden_number}.")