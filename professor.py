import random


def main():

    level = get_level()

    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        print(f"{x} + {y} = ", end="")

        while True:
            for i in range(3):

                guess = input()

                if guess.isalpha():
                    print("EEE")
                    print(f"{x} + {y} = ", end="")

                elif int(guess) == sum:
                    score += 1
                    break

                elif int(guess) != sum:
                    print("EEE")
                    print(f"{x} + {y} = ", end="")

            if int(guess) != sum:
                print(x + y)
                break

            elif int(guess) == sum:
                break


    print("Score:", score)

def get_level():

    # Prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3

    while True:

        try:

            lvl = input("Level: ")

            if int(lvl) == 1:
                return 1

            if int(lvl) == 2:
                return 2

            if int(lvl) == 3:
                return 3

        except ValueError:
            pass


def generate_integer(level):

    # Returns a randomly generated positive integer with "level" digits or raises a ValueError if level is not 1, 2, or 3

    if level == 1:
        level = random.randint(0, 9)
        return level

    elif level == 2:
        level = random.randint(10, 99)
        return level

    elif level == 3:
        level = random.randint(100, 999)
        return level

    else:
        raise ValueError




if __name__ == "__main__":
    main()
