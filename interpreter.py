# Math interpreter
expression = input("Expression: ")
x, y, z = expression.split(" ")

if "+" in y:
    print(round(float(x) + float(z), 1))

elif "-" in y:
    print(round(float(x) - float(z), 1))

elif "/" in y:
    print(round(float(x) / float(z), 1))

elif "*" in y:
    print(round(float(x) * float(z), 1))

else:
    print("Enter a correct mathematical expression.")
