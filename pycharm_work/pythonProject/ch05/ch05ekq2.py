numList = [9,8,7,4,1,3,2,6,5]

i = 0
while i<len(numList)-1 :
    j = i+1
    while j<len(numList) :
        if numList[i] > numList[j] :
            (numList[i], numList[j]) = (numList[j], numList[i])
        j += 1
    i += 1

#for std in numList :
#    print(std)
print(numList)
for i in range(0, len(numList)) :
    for j in range(i+1, len(numList)) :
        if numList[i] > numList[j] :
            (numList[i], numList[j]) = (numList[j], numList[i])

numList.reverse()
print(numList)