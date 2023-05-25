sum = 0


def sub(i):
    global sum
    if i <= 10:
        sum += i
        if i == 10:
            print(i, "=", sum, end="")

        else:
            print(i, "+", end="")

        sub(i + 1)

    else:
        return


sub(1)
