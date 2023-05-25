import sys


stdList = [
    {"seq": 1, "name": "seo", "수학": "95", "국어": "88", "영어": "84"},
    {"seq": 2, "name": "kim", "수학": "88", "국어": "75", "영어": "87"},
    {"seq": 3, "name": "won", "수학": "75", "국어": "75", "영어": "64"},
    {"seq": 4, "name": "park", "수학": "12", "국어": "53", "영어": "35"},
    {"seq": 5, "name": "song", "수학": "99", "국어": "46", "영어": "76"}
]

sequence = 6

def std_list() :
    std_list = []
    seq = 1

    def input_std():
        print("::::: INPUT :::::")
        global sequence
        std = {
            "seq": seq,
            "name": input("성명>>"),
            "kor": int(input("국어점수>>")),
            "eng": int(input("영어점수>>")),
            "mat": int(input("수학점수>>")),
            "total": 0,
            "avg": 0.0,
            "grade": "F",
            "rank": 1
        }
        std["total"] = std["kor"] + std["eng"] + std["mat"];
        std["avg"] = std["total"] / 3.0
        std["grade"] = "A" if std["avg"] >= 90 else (
            "B" if std["avg"] >= 80 else ("C" if std["avg"] >= 70 else ("D" if std["avg"] >= 60 else "F")))

        std_list.append(std)

    input_std();

    print(std_list)

def menu() :
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택: "))
    return no


def title() :
    print("-"*50)
    print("{: ^35}".format(" 누가 대학을 갈까? 사실 다 서울권 가능 "))
    print("-"*50)

def search_list() :
    search_name = input("이름으로 검색 >>")

    while len(search_name) == 0:
        print("입력 하지 않았습니다.")
        search_name = input("이름으로 검색 >>")

    newList = []
    for p in stdList:
        if p['name'] == search_name:
            newList.append(p)

    if len(newList) == 0:
        print("검색 결과 없습니다.")
        return False

    print("{:^3}{:^10}{:^7}{:^5}{:^5}{:^7}{:^7}{:^7}{:^7}".format('no', 'NAME', '수학', '국어', '영어', 'total', 'avg', 'grade', 'rank'))
    print("-" * 50)
    for i, p in enumerate(newList):
        print("{:-^3}{:^10}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}".format(p['seq'], p['name'], p['수학'], p['국어'], p['영어'], p['avg'], p['grade'], p['rank']))

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
                "seq": sequence,
                "name": input("name>> "),
                "수학": input("수학 >> "),
                "국어": input("국어 >> "),
                "영어": input("영어 >> "),
            }

            # 함수 외부 변수(global)는 전변수로 지정 해야 한다.
            # 함수 안에서 함수 외부의 변수를 수정 하기 위해 global 사용.
            sequence = sequence + 1
        elif no == 2 :
            print("=== 출력 기능 ===")
            print("{:^3}{:^10}{:^7}{:^5}{:^5}{:^7}{:^7}{:^7}{:^7}".format('no', 'name', '수학', '국어', '영어', 'total', 'avg', 'grade', 'rank'))
            print("-" * 50)
            for i, p in enumerate(stdList) :
                print("{:-^3}{:^10}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}".format(p['seq'], p['name'], p['수학'], p['국어'], p['영어'],p['total'],  p['avg'], p['grade'], p['rank']))
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
                for p in stdList :
                    if p["seq"] == modify_no :
                        p['name'] = input("새 이름 입력 >>")
                        p['수학'] = input("오류난 수학 입력 >>")
                        p['국어'] = input("오류난 국어 입력 >>")
                        p['영어'] = input("오류난 영어 입력 >>")
                        print("수정 완료!")

        elif no == 5 :
            print("=== 삭제 기능 ===")
            if search_list() :
                modify_no = int(input("삭제 할 no선택 >>"))
                # modify_no로 seq가 같은 요소를 찾는다.
                # seq가 같은 요소의 내용을 새로 입력 받는다.
                for p in stdList :
                    if p["seq"] == modify_no :
                        stdList.remove(p)
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