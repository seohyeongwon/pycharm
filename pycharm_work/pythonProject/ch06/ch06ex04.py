import math

class Circle :
    def __init__(self, r):
        self.r = r
        self.mkArea()
        self.mkLine()

    def mkArea(self):
        self.area = math.pi *self.r**2

    def mkLine(self):
        self.line = 2 * math.pi *self.r

    def __str__(self):
        return "area:%.3f, line:%.3f" %(self.area,self.line)

circle = Circle(10)
print(circle)


class Washer:
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker
    def washing(self):
        detergent()
        print("{} 세탁기 {}킬로 빨래".format(self.maker,self.size))

def detergent():
    print("세제 ㄱㄱ")

washer = Washer(23,"삼성!")
washer.washing()