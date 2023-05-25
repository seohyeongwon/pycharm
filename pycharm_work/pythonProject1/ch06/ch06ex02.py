s="(())()"
def solution(s):

    stack=[]

    for b in s:
        if b=="(":
            stack.append(b)
        else:
            if stack == []:
                #print(False)
                return False
                #break
            else:
                stack.pop()
                #return True
#stack=[]
    if stack != []:
        #print(stack)
        #print(False)
        return False
    else:
        #print(stack)
        #print(True)
        return True
#print(solution)