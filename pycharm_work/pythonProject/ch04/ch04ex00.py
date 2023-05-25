# 생년을 입력 받아서 나이를 환산하는 프로그램
import datetime

print("어서오세요.")
user_name = input("성명을 입력하세요 >>")
print(f"{user_name}님 안녕하세요.")
birth_year = int(input(f"{user_name}님의 출생년도 입력(ex: 1974) >>"))
str_today = str(datetime.date.today())
now_year = int(str_today.split("-")[0])

age = now_year - birth_year
print(f"{user_name}님은 {now_year}년 현재 {age}세입니다.")

if age < 19 :
    print(f"{user_name}님은 미성년자입니다")
else :
    print(f"{user_name}님은 성인입니다")