class Po:
    def __init__(self, gx, gy):
        self.gx = gx
        self.gy = gy

    def sp(self, c="\n"):
        print("x=%d y=%d" %(self.gx, self.gy), end=c)

    def getx(self):
        return self.gx

    def gety(self):
        return self.gy

    def setp(self, gx, gy):
        self.gx = gx
        self.gy = gy


class P3d(Po):
    def __init__(self, gx, gy, gz):
        super().__init__(gx, gy)
        self.gz = gz


    def getz(self):
        return self.gz

    def setp(self, gx, gy, gz):
        super().setp(gx, gy)
        self.gz = gz

    def sp(self):
        super().sp(" ")
        print("z=%d" % self.gz)


p1 = Po(14, 16)
p1.sp()

p1.setp(120, 124)
print(p1.getx(), p1.gety())

p3d = P3d(12, 13, 13)
p3d.sp()

p3d.setp(100, 232, 123)
print(p3d.getx(), p3d.gety(), p3d.getz())
