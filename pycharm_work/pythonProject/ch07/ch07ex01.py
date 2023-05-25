# 객체를 생성하고 사용 하는 부분을 보면
# 클래스를 유추 할 수 있다.
# 아래 클래스 사용부분을 보고 클래스 구현 하시오.
class Car :
    #speed = 0
    def __init__(self, car, year, com, speed):
        self.car = car
        self.year = year
        self.com = com
        self.speed = 20

    def __str__(self):
        print("검색 중...")

        return f"{self.car}, {self.year}, {self.com},{self.speed}"

    def run(self):
        #if self.speed == 0 :
         #   self.speed = 20
        print("{} {} {}가 {} 달림".format(self.car,self.year,self.com,self.speed))

        return self.run

    def speed_up(self):
        self.speed += 10
        return self.speed_up

    def speed_down(self):
        self.speed -= 10
        return self.speed_down


    def stop(self):
        #if self.speed != 0 :
         #   self.speed = 0
        print("{} {} 정지!!".format(self.com,self.car))
        return self.stop

sonata = Car("SONATA", 2019, "HYUNDAI",0)
sonata.run() # 현대 소나타가 2019년이 50킬로로 달린다.

sonata.speed_up()
sonata.run() # 현대 소나타가 2019년이 60킬로로 달린다.

sonata.speed_up()
sonata.run() # 현대 소나타가 2019년이 70킬로로 달린다.

sonata.speed_down()
sonata.speed_down()
sonata.run() # 현대 소나타가 2019년이 50킬로로 달린다.

sonata.stop() # 현대 소나타 정지!


print(sonata.__str__())