name = input("name>>> ")

if len(name) == 1:
    print("1 high")

else:
    age = int(input("age>>> "))
    print(f"{name} {age} {age-10}")

print("finally")