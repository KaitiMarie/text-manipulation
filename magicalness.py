def mockText(changes):
    upper = False
    out = ""
    for char in changes:
        if upper:
            out += char.upper()
        else:
            out += char.lower()
        upper = not upper
    return out

print("Please type a phrase you would like changed")
mode = input("mode: ")
while True:
    if mode == "lower":
        print(input("Lowercase: ").lower())
        #switch to lowercase
    elif mode == "upper":
        print(input("Uppercase: ").upper())
        #switch to upper
    elif mode == "mock":
        print(mockText(input("mock ")))
