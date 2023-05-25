city1 = input("city>>")

if city1 == "서울":
    print(f"{city1} 특별시")

elif city1 in ['서울', '부산', '인천']:
    print(f"{city1} 광역시")

else:
    print("both x")