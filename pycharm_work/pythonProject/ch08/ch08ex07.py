class UDE(Exception):
    def __init__(self,massage):
        super().__init__("사용자 정의 : "+massage)

import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s - %(message)s')

try:
    message = "hihi!!!"
    print(user + message)
    logging.debug(message)
except NameError as q:
    logging.debug("식별자 정의X")
    try:
        raise UDE(str(q))

    except UDE as user_q:
        logging.debug(user_q)
