import sys

name = input("name>>> ")
if len(name)==1:
    print("no name")
    sys.exit()
print(f"{name} {len(name)}")