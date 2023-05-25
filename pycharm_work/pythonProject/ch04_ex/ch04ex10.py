print("money")
mon = int(input("money>>>"))
print("{:-^30}".format("result"))

res = mon

won50000 = res// 50000
res = res%50000

won10000 = res// 10000
res = res%10000

print(f"50000 : {won50000}")
print(f"10000 : {won10000}")
