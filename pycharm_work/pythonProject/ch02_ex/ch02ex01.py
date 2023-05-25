print("성적")
name = input("name")
ko = int(input("ko>>"))
en = int(input("en>>"))
ma = int(input("ma>>"))

total = ko + en + ma
avg = total//3.0

print("---------------")
print(f"{name} ko : {ko} en : {en} ma : {ma}")
print(f"total : {total} avg : {avg}")