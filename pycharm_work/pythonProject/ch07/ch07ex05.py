class Washer :
    def __init__(self,name,maker,do):
        self.name = name
        self.maker = maker
        self.do = do

    def washing(self):
        print(f"{self.name} {self.maker}으로 빨래를 {self.do}kg 중")

washer = Washer("삼송", "트롬", 53)
washer.washing()
