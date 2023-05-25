
class Saram :
    def __init__(self, seq, name, phone):
        self.seq = seq
        self.name = name
        self.phone = phone

    def __str__(self):
        print("자동 호출...")
        return f"{self.seq}, {self.name}, {self.phone}"

    def setSeq(self, seq):
        self.seq = seq

    def setName(self, name):
        self.name = name

    def setPhone(self, phone):
        self.phone = phone

    def getSeq(self):
        return self.seq

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone



class Menu :
    def draw(self):
        print("::::: MENU :::::")
        print("1.input 2.output 3.end")
        return int(input("선택: "))


class List :
    def __init__(self, saram_list):
        self.saram_list = saram_list


    def draw(self):
        print("::::: 사용자 목록 :::::")
        for s in self.saram_list:
            print(s)


class InputSaram :
    def draw(self):
        print("::::: 사람 정보 입력 :::::")


class PhoneBook :
    def __init__(self):
        self.saram_list = [
            Saram(101, "일지매", "010-1010-1010"),
            Saram(102, "홍길동", "010-1010-2222"),
            Saram(103, "이순신", "010-1010-3333")
        ]

        self.factory = [Menu(), InputSaram(), List(self.saram_list)]

        print(":::::: PhoneBook 관리 프로그램 :::::")
        self.play()


    def play(self) :
        no = self.factory[0].draw()
        if no == 3 :
            return

        self.factory[no].draw()
        self.play()





if __name__ == '__main__':
    PhoneBook()