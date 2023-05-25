class Washer :
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker

    def washing(self):
        print(f"{self.maker}이 {self.size}kg 빨래 중")

    def __str__(self):
        return f"size : {self.size} maker : {self.maker}"


wash = Washer( 23,"삼성")
wash.washing()
print(wash)
