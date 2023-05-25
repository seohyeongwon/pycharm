yn ="y"

while yn=="y":

    name = input("name?>>>")
    subj = input("sub?>>>")
    print(f"{name} is {subj}")
    yn = input("y and n")

    while not(yn in ["y", "n"]):
        print("again")
        yn = input("y and n")


