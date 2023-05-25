class People:
    name = None
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름 : {self.name} 나이 : {self.age}"


class Score:
    kor = 0
    eng = 0
    mat = 0
    total = 0

    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.total = self.kor + self.eng + self.mat

    def __str__(self):
        return f"국어 : {self.kor} 영어 : {self.eng} 수학 : {self.mat} 총합 : {self.total} 평균 : {round(self.total / 3,2)}"


class Student:
    hak_no = 0
    person = None
    sung = None

    def __init__(self, hak_no, person, sung):
        self.hak_no = hak_no
        self.person = person
        self.sung = sung

    def __str__(self):
        return f"{self.hak_no} \n{self.person} \n{self.sung}"


student01 = Student(1001, People("홍길동", 24), Score(95, 100, 100))
print(student01)
