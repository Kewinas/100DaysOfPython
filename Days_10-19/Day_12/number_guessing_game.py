import random

print("Welcome to the Number Guessing game!")
print("Im thinking of a number between 1 and 100.")

gameRun = True
diff = input("Choose a difficulty. Type easy/hard: ")
if diff == "hard":
    guesses = 5
else:
    guesses = 10
print(f"You have {guesses} attempts remaining to guess the number.")
number = random.randint(1,100)


while gameRun:
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You guessed right. You have won!")
        gameRun = False
    elif guess > number:
        guesses -= 1
        print("Too high.")
        print("Guess again.")
        print(f"You have {guesses} attempts remaining to guess the number.")
    else:
        guesses -= 1
        print("Too low.")
        print("Guess again.")
        print(f"You have {guesses} attempts remaining to guess the number.")
    if guesses == 0:
        print("No more guesses left. You lost!")
        gameRun = False

