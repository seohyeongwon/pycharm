def player(callback):
    try :
        print("{:-^30}".format("try"))
        print("예외 발생 가능성 있으면 try")
        re = callback()
        print("처리 결과 : ", re)
    except TypeError:
        print("{:-^30}".format("except TE"))
        print("TE 예외 발생 실행됨")
        print("예외 : callback은 함수 아님")
        print(callback)
    except :
        print("{:-^40}".format("ex TE"))
        print("TE 예외 이외의 예외")
    else:
        print("{:-^30}".format("else"))
        print("예외 발생 안됨")
    finally:
        print("{:-^30}".format("finally"))
        print("에러 발생여부 관계없이 마무리 작업")

def sayHello():
    return "Hello World"

#player(sayHello)
#player("Hello")
player(sayHello())