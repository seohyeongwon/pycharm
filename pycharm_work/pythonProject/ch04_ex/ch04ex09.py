sco = int(input("sco>>>"))
gra = "f"

if sco >101  or sco<0:
    print("err")
else:

    if sco >= 80:
        gra = "b"
    elif sco >= 70:
        gra = "c"
    else :
        gra = "f"

print(f"{sco} {gra}")