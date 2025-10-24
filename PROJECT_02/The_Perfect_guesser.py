import random

n = random.randint(1, 100)
guess = None
attempts = 0

while guess != n:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1
    if guess < n:
        print("Higher number, Please!")
    elif guess > n:
        print("Lower number, Please!")

print(f"Congratulations! You've guessed the number {n} in {attempts} attempts.")