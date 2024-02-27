camel = input("camelCase: ")

x = ""
for i in camel:
    if (i.isupper()):
        x += "_" + i
        camel = x

    else:
        x += i

snake = x.lower()

print("snake_code: ", snake)
