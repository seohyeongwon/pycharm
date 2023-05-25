import sys

sequence = 1
std_list = [
    #{"seq": 1, "name": "HONG", "kor": 90, "eng": 90, "mat": 90, "total": 270, "avg": 90.0, "grade": "A", "rank": 1},
    #{"seq": 2, "name": "KIM", "kor": 90, "eng": 90, "mat": 90, "total": 270, "avg": 90.0, "grade": "A", "rank": 1},
    #{"seq": 3, "name": "LEE", "kor": 90, "eng": 90, "mat": 90, "total": 270, "avg": 90.0, "grade": "A", "rank": 1}
]

def title():
    print("-" * 50)
    print("{: ^40}".format("수능 전 9평 서연고 마지막"))


def input_std():
    global sequence
    print(" ------ 입력해 ------ ")
    std = {
        "seq": sequence,
        "name": input("이름>>>>"),
        "kor": int(input("국어점수>>")),
        "eng": int(input("영어점수>>")),
        "mat": int(input("수학점수>>")),
        "total": 0,
        "avg": 0.0,
        #"grade": "F"
    }
    std["total"] = std["kor"] + std["eng"] + std["mat"]
    std["avg"] = round(std["total"] / 3.0,3)
    #std["grade"] = "A" if std["avg"] >= 90 else (
        #"B" if std["avg"] >= 80 else ("C" if std["avg"] >= 70 else ("D" if std["avg"] >= 60 else "F")))
    std_list.append(std)
    sequence = sequence + 1


def menu(*menuItemList):
    print("{:-^50}".format(menuItemList[0]))
    for i, item in enumerate(menuItemList):
        if i != 0:
            print(i, ".", item, sep="", end=" ")
    no = int(input("\n선택: "))
    while not (no in range(1, len(menuItemList))):
        print("입력 범위를 초과 했습니다. ({}~{}사이 입력)".format(1, len(menuItemList) - 1))
        no = int(input("다시 선택: "))
    return no


def search_list_name():
    search_name = input("이름 검색 >>")
    while len(search_name) == 0:
        print("검색어를 입력 하지 않았습니다.")
        search_name = input("이름으로 검색 >>")

    newList = []
    for s in std_list:
        if s['name'] == search_name:
            newList.append(s)

    if len(newList) == 0:
        print("검색 결과 없습니다.")
        return False

    print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format('seq', 'name', 'kor', 'eng', 'mat',
                                                                                  'total', 'avg'))
    print("_" * 75)
    for i, s in enumerate(newList):
        print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format(s['seq'], s['name'], s['kor'],
                                                                                      s['eng'], s['mat'], s['total'],
                                                                                      s['avg']))

    return True


def student():
    title()
    global seq
    while True:
        no = menu("MENU", "입력", "출력", "검색", "수정", "삭제", "종료")
        if no == 1:
            input_std()
        elif no == 2:
            print("::::: 출력 기능 :::::")
            print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format('seq', 'name', 'kor', 'eng',
                                                                                          'mat', 'total', 'avg'))
            print("_" * 75)
            for i, s in enumerate(std_list):
                print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format(s['seq'], s['name'],
                                                                                              s['kor'], s['eng'],
                                                                                              s['mat'], s['total'],
                                                                                              s['avg']))
        elif no == 3:
            print("::::: 검색 기능 :::::")
            search_list_name()
        elif no == 4:
            print("::::: 수정 기능 :::::")
            print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format('seq', 'name', 'kor', 'eng',
                                                                                          'mat', 'total', 'avg'))
            print("_" * 75)
            for i, s in enumerate(std_list):
                print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format(s['seq'], s['name'],
                                                                                              s['kor'],
                                                                                              s['eng'], s['mat'],
                                                                                              s['total'],
                                                                                              s['avg']))
            if search_list_name():
                seq = int(input("수정 할 seq번호 입력 >>"))
                for p in std_list:
                    if p["seq"] == seq:
                        s_no = menu("수정 선택", "이름수정", "국어점수 수정", "영어점수 수정", "수학점수 수정")
                        if s_no == 1:
                            p["name"] = input("새 이름 입력 >>")
                        elif s_no == 2:
                            p["kor"] = int(input("새 국어점수 입력 >>"))
                            p["total"] = p["kor"] + p["eng"] + p["mat"]

                        elif s_no == 3:
                            p["eng"] = int(input("새 영어점수 입력 >>"))
                            p["total"] = p["kor"] + p["eng"] + p["mat"]
                            p["avg"] = round(p["total"] / 3.0,3)

                        elif s_no == 4:
                            p["mat"] = int(input("새 수학점수 입력 >>"))
                            p["total"] = p["kor"] + p["eng"] + p["mat"]
                            p["avg"] = round(p["total"] / 3.0,3)

                        else:
                            print("해당 사항 없습니다!")
        elif no == 5:
            print("::::: 삭제 기능 :::::")
            print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format('seq', 'name', 'kor', 'eng',
                                                                                          'mat', 'total', 'avg'))
            print("_" * 75)
            for i, s in enumerate(std_list):
                print("{: <3}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format(s['seq'], s['name'],
                                                                                              s['kor'],
                                                                                              s['eng'], s['mat'],
                                                                                              s['total'],
                                                                                              s['avg']))
            if search_list_name():
                del_no = int(input("삭제 할 no선택 >>"))
                for p in std_list:
                    if p["seq"] == del_no:
                        std_list.remove(p)
                        print("삭제완료!")
                        break
        elif no == 6:
            print("----- END -----")
            print("----- 프로그램 종료 -----")
            print("빠잉")
            sys.exit(0)
        else:
            pass


if __name__ == '__main__':
    student()
