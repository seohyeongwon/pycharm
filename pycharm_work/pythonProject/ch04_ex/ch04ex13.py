


while True:
    wo = input("word>>>")
    if wo == "stop" :
        break
    if len(wo)<3 :
        print(f"{wo} so short")
    elif len(wo)>10:
        print(f"{wo} so long")
    else:
        print(f"{wo}")

print("end")