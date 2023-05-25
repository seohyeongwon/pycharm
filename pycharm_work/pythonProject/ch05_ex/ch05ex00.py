import random

lot = set()

while len(lot) < 6:
    lot.add(random.randint(1,45))

print("--- lottp ---")

for i in lot:
    print(i, end="  ")