# Counts the amount of lines in a given file, not counting comments or \n

import sys


while True:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 2:
        file = sys.argv[1]
        if not file.endswith("py"):
            sys.exit("Not a Python file")
        else:
            break

try:

    program = open(file)

except FileNotFoundError:
    sys.exit("File does not exist")

lines = 0

for line in program.readlines():
    if line.isspace() == True:
        lines += 0
    elif line.lstrip().startswith("#") == True:
        lines += 0
    else:
        lines +=1

program.close()
print(lines,)
