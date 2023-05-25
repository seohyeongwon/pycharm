gra = "f"

sco = int(input("sco>>>"))

while not(sco in range(0,101)):
    print("err")
    sco = int(input("retry>>>"))

if sco >= 90 :
    gra = "a"
elif sco >= 80 :
    gra = "b"
else :
    gra = "c"

num = sco % 10
if num>7 :
    gra = str(gra) + "+"
elif num<3:
    gra =str(gra) + "="

print(f"{sco} {gra}")