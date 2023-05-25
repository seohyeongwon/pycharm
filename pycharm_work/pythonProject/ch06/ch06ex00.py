addrList = [
    {"idx": 0, "name": 'HONG', "phone": '010-111-111',"addr": '서울시 마포구'},
    {"idx": 1, "name": 'KIM', "phone": '010-111-111',"addr": '서울시 마포구'},
    {"idx": 2, "name": 'LEE', "phone": '010-111-111',"addr": '서울시 마포구'}
]
idx = 2;

def menu() :
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택>>> "))
    return no


def mkData() :
    global idx
    idx +=1
    name = int(input("성명입력>>> "))
    phone = int(input("전화번호입력>>> "))
    addr = int(input("주소입력>>> "))

    return {"idx": idx, "name": "name","phone": "phone" ,"addr": addr}

def inputData() :
    print("### 입력 기능 ###")
    data_value = mkData()
    addrList.append(data_value)
    print("데이터 입력 성공!")

def outputData() :
    print("### 출력 기능 ###")
    for person in addrList :
        print("{: ^3}|{: ^6}|{: ^13}|{: ^9}".format(person["idx"],person["name"],person["phone"],person["addr"]))

def find_idx(addrList, idx=None, name=None) :
    flag = 0
    if name != None :
        flag = 1

    for i, person in enumerate(addrList) :
        if flag ==0 :
            if person["idx"] == idx :
                return i
            else :
                if person["name"] == name :
                    return i
    return -1

def seachData():
    print("### 검색 기능 ###")
    searchName = input("검색 할 이름을 입력하세요 : ")
    index = find_idx(addrList, name=searchName)
    person = addrList[index]
    print("{: ^3}|{: ^6}|{: ^13}|{: ^9}".format(person["idx"], person["name"], person["phone"], person["addr"]))

def modifyData() :
    print("### 수정 가능 ###")

def deletData() :
    print("### 삭제 기능 ###")
    # del addrList[1]
    del_idx = int(input("삭제 할 번호를 입력하세요 : "))
    index = find_idx(addrList, idx=del_idx)
    if index != -1 :
        del addrList[index]
        print("삭제 성공!")
    else:
        print("삭제 할 대상이 없습니다!")

factory = [inputData, outputData, seachData, modifyData, deletData]

def run(no) :
    print("{}번이 선택되었습니다!".format(no))
    if no == 6 :
        print("### 종료 ###")
        exit(0)

        if no in range(1, len(factory)+1) :
            factory[no-1]()
        else:
            print("해당 사항 없음");

def main() :
    while True :
        print("{:=^40}".format(" 주소록 "))
        no = menu()

        run(no)
        print("\n")

if __name__ == '__main__' :
    main()

