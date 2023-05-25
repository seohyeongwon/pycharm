import sys

name = input("이름")
if len(name) == 0 :
    print("no")
    sys.exit()
print("{} {}".format(name, len(name)))
