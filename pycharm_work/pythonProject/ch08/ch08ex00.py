import logging
from time import sleep

while True:
    try:
        age = int(input("나이>>> "))
        print("나이는? " , age)
        break
    except ValueError as e :
        logging.warning("정수!");
        sleep(0.5)
        continue

print("end!!")