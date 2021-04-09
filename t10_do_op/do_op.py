print("---- Simple calculator ----")
print("Let's add some numbers")
a = input("Input your first value: ")
op = input("Input your operator: ")
if (op == "+" or op == "-" or op == "*" or op == "/"):
    b = input("Input your second value: ")
    if (a.isnumeric() and b.isnumeric()):
        a = int(a)
        b = int(b)
        if (op == "+"):
            res = a + b
        elif (op == "-"):
            res = a - b
        elif (op == "/"):
            res = a / b
        elif (op == "*"):
            res = a * b
        print(f"{a} {op} {b} = {res}")
    else:
        print("Enter correct numbers")
else:
    print("usage: the operator must be '*' or '+' or '-' or '/'")
print("---- Simple calculator ----")
