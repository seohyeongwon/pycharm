lis = [
    {"seq":1, "name":"sonata", "price": 1800},
    {"seq":2, "name":"그랜저", "price": 2500},
    {"seq":3, "name":"벤츠", "price": 7000},
    {"seq":4, "name":"BMW", "price": 5000}
]

# w모드는 쓰기모드
# 쓰기모드는 자동 파일 생성
with open("car.data", "w", encoding="UTF-8") as fp :
    for car in lis:
        fp.write(f'{car["seq"]}|{car["name"]}|{car["price"]}\n')


print("파일 기록 성공")