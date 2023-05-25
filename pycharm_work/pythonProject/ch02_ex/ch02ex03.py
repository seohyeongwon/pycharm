print("3개 정수")
one = int(input("1>>"))
two = int(input("2>>"))
thr = int(input("3>>"))

max_n = max(one, max(two, thr))
min_n = min(one,min(two, thr))

print(f"big %d" %max_n)
print(f"min %d" %min_n)