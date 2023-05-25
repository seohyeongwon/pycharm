qwe = open("op_01","w", encoding="utf-8")


qwe.write("{:-^38}\n".format("프로필"))
qwe.write("{:-^10}{:-^10}{:-^10}{:-^10}\n".format("이름","나이","ph", "주소"))

name = input("이름>>> ")
age = input("나이>>> ")
ph = input("ph>>> ")
addr = input("주소>>> ")


qwe.write(f"name : {name}\t")
qwe.write(f"age : {age}\t")
qwe.write(f"ph : {ph}\t")
qwe.write(f"addr : {addr}\t")


qwe.close()