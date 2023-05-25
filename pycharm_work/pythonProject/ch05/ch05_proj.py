"""
--------------- Todo List ---------------
[1] (완) 친구 만나기
[2] (미) 과제 하기
[3] (미) 청소 하기
[4] (완) 붕어 밥 주기

------------------ MENU ----------------
1.입력 2.수정
선택: 1

------------------ INPUT ----------------
할일 : 여행 하기

--------------- Todo List ---------------
[1] (완) 친구 만나기
[2] (미) 과제 하기
[3] (미) 청소 하기
[4] (완) 붕어 밥 주기

------------------ MENU -----------------
1.입력 2.수정
선택: 2

----------------- MODIFY -----------------
수정 할 항목 번호 입력 : 3
[3] (미) 청소하기

------------------ MENU -----------------
1.상태수정 2.할일수정 3.삭제
선택: 1

--------------- Todo List ---------------
[1] (완) 친구 만나기
[2] (미) 과제 하기
[3] (완) 청소 하기
[4] (완) 붕어 밥 주기

------------------ MENU -----------------
1.입력 2.수정
선택: 2

----------------- MODIFY -----------------
수정 할 항목 번호 입력 : 3
[3] (완) 청소하기

------------------ MENU -----------------
1.상태수정 2.할일수정 3.삭제
선택: 2
할일 입력: 청소하기 2
--- 삭제 완료 ---

--------------- Todo List ---------------
[1] (완) 친구 만나기
[2] (미) 과제 하기
[3] (완) 청소 하기 2
[4] (완) 붕어 밥 주기

------------------ MENU ----------------
1.입력 2.수정
선택: 2

----------------- MODIFY -----------------
수정 할 항목 번호 입력 : 3
[3] (완) 청소하기

------------------ MENU ----------------
1.상태수정 2.할일수정 3.삭제
선택: 3
--- 삭제 완료 ---

--------------- Todo List ---------------
[1] (완) 친구 만나기
[2] (미) 과제 하기
[4] (완) 붕어 밥 주기

------------------ MENU ----------------
1.입력 2.수정
선택:
"""

todo_list = [
    {"seq":1, "title":"친구 만나기", "done":True},
    {"seq":2, "title":"과제 하기", "done":False},
    {"seq":3, "title":"붕어 밥 주기", "done":False}
]
sequence = 4
select_todo = None


def print_row(item) :
    print("[{0}] ({1}){2}".format(item['seq'], "완" if item['done'] else "미", item['title']))


def print_list() :
    print("{:-^40}".format(" Todo List "))
    for i, item in enumerate(todo_list) :
        print_row(item)


def menu(menu_item) :
    for i, item in enumerate(menu_item) :
        if i == 0 :
            print("{:-^40}".format(f" {menu_item[0]} "))
        else :
            print(f"{i}.{menu_item[i]}", end=" ")

    no = int(input("\nChoice: "))
    while(not(no>0 and no<len(menu_item))) :
        print(f"입력 오류: {1} ~ {len(menu_item)-1}사이만 입력하세요!")
        no = int(input("Choice: "))

    return no


def insert_todo() :
    print("::::: 입력 기능 :::::")


def modify01() :
    print("::::: 상태 수정 기능 :::::")
    select_todo['done'] = not(select_todo['done'])

def modify02() :
    print("::::: 할일 수정 기능 :::::")
    select_todo['title'] = input("할 일 다시 입력:")


modify_fn_factory = [None, modify01, modify02]


def modify_todo() :
    # 함수 외부에 선언 된 전역(global) 변수를 수정 하기 위해서는
    global select_todo

    seq = int(input("수정 할 항목 번호 입력: "))
    print_row(select_todo)

    for item in todo_list :
        if seq == item['seq'] :
            select_todo = item
            print("찾았습니다!!")
            break


    if select_todo != None :
        while True :
            menu_list = ["MODIFY MENU", "상태수정", "할일수정", "삭제", "확인"]
            no = _factory[0](menu_list)
            print("------> ", no)
            if no == len(menu_list) - 1:
                print("--- 실행 취소 - main으로 이동 합니다 ---")
                return

            if no == 3:
                todo_list.remove(select_todo)
                print("--- 삭제 성공! - main으로 이동 합니다 ---")
                return

            modify_fn_factory[no]() # 함수에 괄호를 붙여야 실행이다.

    else :
        print("선택 항목은 목록에 없습니다!")


# List 구조에 함수를 저장
_factory = [menu, insert_todo, modify_todo]


def main() :
    while True :
        print_list()
        menu_list = ["MENU", "입력", "수정","종료"]
        # 0번째는 Title, 마직막은 "종료"가 들어가도록 한다.
        no = _factory[0](menu_list)
        print("선택 한 번호는", no)
        if no == len(menu_list)-1 :
            print("--- 프로그램 종료 ---")
            break

        print("=" * 40)
        _factory[no]()
        print("=" * 40)


if __name__ == '__main__' :
    res = main()






# 좋은 소프트웨어를 구현하기 위한 원칙 (고전적인)
# 루즈 커플링 == 의존성은 낮추고 응집력은 높이다.
# 객체지향 SOLID 5대 원칙
# 1. 단일 책임 원칙 (SRP)
# 2. 개방 폐쇄 원칙 (OCP)
# 3. 리스코프 치환 원칙 (LSP)
# 4. 인터페이스 분리 원칙 (ISP)
# 5. 의존관계 역전 원칙 (DIP)