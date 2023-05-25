import logging
import time

fish_list =['오징어', '꼴뚜기', '대구', '명태', '거북이']
print("생선 주문!!!")
for i, fish in enumerate(fish_list) :
    print(f"({i+1}) {fish} ", end="")

while True :
    try :
        choice = int(input(">>>>>> "))
        print('-' *55)
        print(fish_list[choice - 1], end="")
        break

    except IndexError:
        logging.error("IE 발생")
        print("다시 선택", end="")

    except ValueError:
        logging.error("VE 발생")
        time.sleep(0.1)
        print("다시 선택", end="")

print("정상 주문 완료!!!!")