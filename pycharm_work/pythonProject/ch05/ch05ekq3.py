# 선택정렬 연습
# 선택정렬, 삽입정렬, 버블정렬

numList = [9,8,7,4,1,3,2,6,5]
newList = [0,0,0,0,0,0,0,0,0]
# 정렬 되도록 출력하라.
# for문을 이용 해 볼 것

for i in range(0, len(newList)) :
    m = min(numList)
    newList[i] = m
    numList.remove(m)

print(newList)
