import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100!")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess == number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
