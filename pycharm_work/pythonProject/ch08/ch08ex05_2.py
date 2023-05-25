uname = input("name>>> ")

try:
    assert len(uname)>=2,"name 1"
    print("you name : ", uname)
except AssertionError as q :
    print(q)