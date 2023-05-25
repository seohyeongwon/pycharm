full = input("문자열>>")
old = input("old>>")
new = input("new>>")

st = full.index(old)
end = st + len(old)

re = full[:st] + new + full[end:]
print(re)