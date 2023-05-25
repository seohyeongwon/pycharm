name = input("name>>>>> ")

while True :
    try :
        age = int(input("age>>>>> "))
        print(name + "님은", end="")
        if age < 20:
            print("민짜")
        elif age < 41:
            print("청년")
        elif age < 70:
            print("중년")
        else:
            print("노인")
        break
    except :
        print("ValueError 다시")
        continue