class UDE(Exception) :
    def __init__(self,mess):
        super().__init__("예외: "+ mess)

try:
        mess = user + "hihi!!!"
        print(mess)

except NameError as q:
        print("식별자 안됨")

        try:
            raise UDE(str(q))
        except UDE as user_q:
            print(user_q)