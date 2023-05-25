class Po:
    def __init__(self, gx, gy):
        self.gx = gx
        self.gy = gy

    def sp(self):
        print("x=%d y=%d" % (self.gx, self.gy))

    def getx(self):
        return self.gx

    def gety(self):
        return self.gy


    def setp(self, gx, gy):
        self.gx = gx
        self.gy = gy


p1 = Po(14, 16)
p1.sp()

p1.setp(120, 124)
print(p1.getx(), p1.gety())
