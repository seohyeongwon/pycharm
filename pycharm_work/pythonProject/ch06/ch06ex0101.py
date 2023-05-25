sum = 0
def sub(i):
    global sum
    if i<=10:

        sum += i

        "=" if i == 10 else "+"

        sub(i+1)

    else :
        print("=", sum)
        return
sub(1)
"""
if i == 10 :
    print(i,"=", sum,end="")

else:
    print(i,"+", end="")
"""