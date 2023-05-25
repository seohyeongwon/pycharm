name = "홍길동"
age = 26

print(name, "님은", age, "세 입니다.", sep="", end='@@@@\n')
print("%s님은 %d세 입니다" %("서형원", 20))
print("{}님은 {}세" .format("서형원", 21))
print(f"{name}님 {age}세")

infoData = """ 

주소: {}
전화번호: {}
""" .format("서울시 강남구","010-1234-7890")
print(infoData)

sql= """ 
qwer"""
