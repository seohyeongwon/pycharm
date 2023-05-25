import random
import sys

k = random.randint(1, 100)
numbers = 0;
cnt = 0;
size = 5;
min = 1;
max = 100
yn = "y"

print(f"숫자 선택... 완료 해보셈>> (힌트: {k})")
numbers = int(input(f"{min}~{max} 사이 입력"))
while not(numbers in range(min, max)) :
    print(("범위 초과~! 다시 입력>>"))
    numbers = int(input(f"{min}~{max} 사이 입력"))
while True :
    if numbers<k :
        print("high")
        min = numbers
        numbers = int(input(f"{min}~{max} 사이 : "))
    elif numbers>k:
       print("low")
       max = numbers
       numbers = int(input(f"{min}~{max} 사이 : "))
    elif numbers==k :
        yn = input("wow \n한번더? y/n")
        if yn == 'y' :
           main()
        elif yn == 'n' :
            print("bye")
            sys.exit()
main()