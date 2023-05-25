po =[]
ne = []

for i in range(5):
    num = int(input(f"int{i+1}>>>"))

    if num>0 :
        po.append(num)
    else:
        ne.append(num)

print(f"po: {po}")
print(f"no: {ne}")