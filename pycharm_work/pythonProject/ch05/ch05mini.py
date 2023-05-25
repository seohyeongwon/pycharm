import sys


pList = [
    {"seq":1, "name":"HONG", "phone":"010-1111-1111", "addr":"서울시 강남구"},
    {"seq":2, "name":"KIM", "phone":"010-1111-2222", "addr":"대구시 수성구"},
    {"seq":3, "name":"LEE", "phone":"010-1111-3333", "addr":"부산시 사하구"},
    {"seq":4, "name":"PARK", "phone":"010-1111-4444", "addr":"광주시 송정동"}
]

sequence = 5

def menu() :
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택: "))
    return no


def title() :
    print("-"*50)
    print("{: ^50}".format(" 주소록 "))
    print("-"*50)


def search_list() :
    search_name = input("이름으로 검색 >>")
    while len(search_name) == 0:
        print("검색어를 입력 하지 않았습니다.")
        search_name = input("이름으로 검색 >>")

    newList = []
    for p in pList:
        if p['name'] == search_name:
            newList.append(p)

    if len(newList) == 0:
        print("검색 결과 없습니다.")
        return False

    print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format('no', 'NAME', 'PHONE', 'ADDRESS'))
    print("-" * 60)
    for i, p in enumerate(newList):
        print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format(p['seq'], p['name'], p['phone'], p['addr']))

    # 검색 결과가 있을 경우 True 반환
    return True

def process() :
    global sequence

    title()

    while True :
        no = menu()
        print(f"{no}번을 선택 했습니다.")

        if no == 1 :
            print("=== 입력 기능 ===")
            p = {
                "seq":sequence,
                "name": input("성명 입력>> "),
                "phone": input("전화 번호 입력>> "),
                "addr": input("주소 입력>> ")
            }
            pList.append(p)
            # 함수 외부 변수(global)는 전변수로 지정 해야 한다.
            # 함수 안에서 함수 외부의 변수를 수정 하기 위해 global 사용.
            sequence = sequence + 1
        elif no == 2 :
            print("=== 출력 기능 ===")
            print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format('no', 'NAME', 'PHONE', 'ADDRESS'))
            print("-" * 60)
            for i, p in enumerate(pList) :
                print("{: <3}|{: ^10}|{: ^20}|{: ^30}".format(p['seq'],p['name'], p['phone'], p['addr']))
        elif no == 3 :
            print("=== 검색 기능 ===")
            # 이름으로 검색 : LEE
            # pList의 요소 중 name이 LEE인 요소를 새 리스트에 저장.
            # 새 리스트 출력
            search_list()

        elif no == 4 :
            print("=== 수정 기능 ===")
            if search_list() :
                modify_no = int(input("수정 할 no선택 >>"))
                # modify_no로 seq가 같은 요소를 찾는다.
                # seq가 같은 요소의 내용을 새로 입력 받는다.
                for p in pList :
                    if p["seq"] == modify_no :
                        p['name'] = input("새 이름 입력 >>")
                        p['phone'] = input("새 전화 입력 >>")
                        p['addr'] = input("새 주소 입력 >>")
                        print("수정 완료!")

        elif no == 5 :
            print("=== 삭제 기능 ===")
            if search_list() :
                modify_no = int(input("삭제 할 no선택 >>"))
                # modify_no로 seq가 같은 요소를 찾는다.
                # seq가 같은 요소의 내용을 새로 입력 받는다.
                for p in pList :
                    if p["seq"] == modify_no :
                        pList.remove(p)
                        print("삭제 완료!")
                        break

        elif no == 6 :
            print("--- 프로그램 종료 ---")
            print("다음에 만나요.")
            sys.exit(0);
            break

        else :
            print("해당 사항 없습니다!")

        print("\n")


if __name__ == '__main__' :
    process()