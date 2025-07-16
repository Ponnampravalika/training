import random
secret_number = random.randint(1, 100)
print("Guess the number (between 1 and 100)")
while True:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        break
