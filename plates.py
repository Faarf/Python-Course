def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def punc(n):
    marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in n:
        if i in marks:
            return False

def number(s):
    for i in s:
        if i.isdigit() and i == "0":
            return False
        elif i.isdigit() and i != "0":
            break


def medium(s):
    i = 0
    while i < len(s) - 1:
        if not s[i].isalpha():
            if s[i] == "0":
                return False
            elif not s[i:].isdigit():
                return False
            else:
                return True
        i += 1

def is_valid(s):

# Start with 2 letters

    if s[0:2].isalpha() == False:
        return False

# Maximum 6 letters (min 2 letters)
    elif len(s) < 2 or len(s) > 6:
        return False

# Numbers must be at the end, not in the middle or start
    elif medium(s) == False:
        return False

# The number can't start with an "0"
    elif number(s) == False:
        return False

# No spaces or puncutation marks
    elif punc(s) == False:
        return False

    else:
        return True

main()
