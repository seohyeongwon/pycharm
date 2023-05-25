import random

lis = [1,2,3,4,5,6,7,8,9,10]
total = 0

print(lis)

for i in range(4):
    num = int(random.choice([1,2,3,4]))
    print(num,end="\n")

    total += num

print(f"={total}")
