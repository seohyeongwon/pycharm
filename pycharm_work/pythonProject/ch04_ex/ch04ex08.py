sco = int(input("sco>>>"))
gra = "f"

if sco >= 90 :
    gra = "a"
elif sco >= 80:
    gra = "b"
elif sco >= 70:
    gra = "c"
else :
    gra = "a"

print(f"{sco} {gra}")