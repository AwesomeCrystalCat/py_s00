str_1 = input("Enter your first string: ")
str_2 = input("Enter your second string: ")

if not str_1 or not str_2:
    print("One of the strings is empty.")
else:
    cmd = input("Enter your command: ")

    if (cmd == "concat"):
        print(f"Your string is: {str_1} {str_2}")
    elif (cmd == "find"):
        print(str_2 in str_1)
    elif (cmd == "beatbox"):
        num_1 = input("Enter your first beatbox number: ")
        num_2 = input("Enter your second beatbox number: ")

        if (num_1.isnumeric() and num_2.isnumeric()):
            num_1 = int(num_1)
            num_2 = int(num_2)
            print(f"{str_1 * num_1}{str_2 * num_2}")
        else:
            print("Enter correct numbers, human!")
    else:
        print("usage: command find | concat | beatbox")

