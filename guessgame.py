import random

while True:

    try:
        level = int(input("Level: "))
        if level > 0:
            break

    except ValueError:
        pass

number = random.randrange(1, level)

while True:

    try:

        guess = int(input("Guess: "))

        if guess == number:
            print("Just right!")
            break

        elif guess > number:
            print("Too large!")

        elif guess < number:
            print("Too small!")

    except (NameError, ValueError):
        pass


