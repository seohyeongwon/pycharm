# 클래스 만들기 연습
# 급하면 망한다.
# 안되면 한번더!
# 비법은 연습이다.
class TV:
    # 생성자, 필드, 메소드를 구현 하시오.
    name = None
    channel = 11
    speaker = None

    def __init__(self, name, speaker):
        # 생성자가 하는 일은 필드 초기화
        self.name = name
        self.speaker = speaker
        print(f"{self.name} TV 생성")

    def powerOn(self):
        print(f"{self.name} TV 켜기")

    def volumeUp(self):
        self.speaker.volumeUp()

    def volumeDown(self):
        self.speaker.volumeDown()

    def powerOff(self):
        print(f"{self.name} TV 끄기")

class Speaker:
    volume = 3
    name = None

    def __init__(self, name):
        self.name = name

    def volumeUp(self):
        self.volume += 1
        print(f"{self.name} 소리 키우기 volume: {self.volume}")

    def volumeDown(self):
        self.volume -= 1
        print(f"{self.name} 소리 줄이기기 volume: {self.volume}")


samsungTV = TV("삼성", Speaker("Sony"))  # 삼성 TV 생성 ---> def __init__(self) :

samsungTV.powerOn()  # 삼성 TV 켜기
samsungTV.volumeUp()  # 삼성 TV 소리 키우기 volume: 6
samsungTV.volumeDown()  # 삼성 TV 소리 줄이기 volume: 5
samsungTV.powerOff()  # 삼성 TV 끄기