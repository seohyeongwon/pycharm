class Super :
    def __init__(self, name):
        self.name = name
    def show(self):
        print('name -->', self.name)

class Sub(Super):
    def __init__(self,name,job):
        super().__init__(name)
        self.job = job
    def show(self):
        super().show();
        print('job-=->',self.job)
        print(self.name+" 직업은 "+self.job+"임")

if __name__ == '__main__':
    person = Sub("홍길동","도둑")
    person.show()

