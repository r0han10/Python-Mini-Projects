import random

Lowest_num = 1
Highest_num = 100
answer = random.randint(Lowest_num, Highest_num)

guesses = 0

is_running = True
print("*****NUMBER GUESSING GAME*****")
print()
print(f"Select any random number between {Lowest_num} and {Highest_num}")

while is_running:

    guess = input("Enter your guess: ")  # * If we use  guess = int(input()) element, then the game will crash
    # *           if someone input somthing else than an integer

    if guess.isdigit():
        guess = int(guess)  # ! We have to convert this into an integer
        guesses += 1

        if guess < Lowest_num or guess > Highest_num:  # todo: you have to use 'or' operator, something else will be invalid.For instance, using and will ruin these 4 lines of code. Because there is no such number which is lower and higher at the same time.
            print("That number is out of range.")
            print(f"Please select any random number between {Lowest_num} and {Highest_num}")

        elif answer < guess:
            print("Too high! Try again!")
        elif answer > guess:
            print("Too low! Try again!")
        else:
            print("______YOU WIN______")
            print()
            print(f"The answer was {answer}")
            print(f"Your total guesses number is {guesses}")
            is_running = False
    else:
        print("Your Guess is INVALID ! ")
        print(f"Please select any random number between {Lowest_num} and {Highest_num}")

