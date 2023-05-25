# 클래스 만들기 연습
class TV :
    # 생성자, 필드, 메소드를 구현 하시오.
    def __init__(self, name, vol=7):
        self.name = name
        self.vol = 7
        print(f"{self.name} 생성")

    def __str__(self):
        print("검색 중...")

        return f"{self.name}, {self.vol}"

    def powerOn(self):
        print(f"{self.name} 켜짐")

    def volumeUp(self):
        self.vol += 1
        print(f"{self.name} 소리 키움 vol : {self.vol}")

    def volumeDown(self):
        self.vol -= 1
        print(f"{self.name} 소리 작아짐 vol : {self.vol}")

    def powerOff(self):

        print(f"{self.name} 꺼짐")

samsungTV = TV("삼성") # 삼성 TV 생성

samsungTV.powerOn() # 삼성 TV 켜기

samsungTV.volumeUp() # 삼성 TV 소리 키우기 volume: 6
samsungTV.volumeDown() # 삼성 TV 소리 줄이기 volume: 5

samsungTV.powerOff() # 삼성 TV 끄기

print(samsungTV)