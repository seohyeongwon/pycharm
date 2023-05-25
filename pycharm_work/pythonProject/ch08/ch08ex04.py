class UserDeError(Exception):
    pass

try:
    raise UserDeError("user error!!!!!!!!")
except UserDeError as q :
    print(q)