movieList = ["1","2","3","4","5"]
print("0. 리스트 : ", movieList)
print("1. 리스트 1 : ", movieList[0])
print("2. 리스트 2 : ", movieList[len(movieList)-1])
movieList[1] = "12222"
print("3. 리스트 3: ", movieList)
del movieList[2]
print("4. 삭제 : ", movieList)
movieList.append("666")
print("5. 추가 : ", movieList)
movieList.insert(2, 22221414)
print("6. 추가 : ", movieList)
print("7. 위치 : ", movieList.index("12222"))
