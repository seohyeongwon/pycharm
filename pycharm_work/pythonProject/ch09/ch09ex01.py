def say_hello(name) :
    print("hello", name)

def say_hello2(name):
    print("good", name)

#main 블럭에서 사용하지 않으면 import 순간 바로 실행 됨
#say_hello("qwe")
#say_hello2("asd")

if __name__ == '__main__' :
    say_hello("kim")
    say_hello2("hong")