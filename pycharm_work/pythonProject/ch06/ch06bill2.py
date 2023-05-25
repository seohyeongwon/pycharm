from datetime import datetime

"""
{
    "o_seq": 1, # 주문 고유 번호
    "o_name" : "", # 주문 상품 명
    "o_option" : [], # 주문 옵션
    "ea_price": 0, # 개당 가격
    "cnt" : 0 # 수량
}
"""
card_info = {
    "카드번호": "",
    "카드사" : "삼성비자카드",
    "카드종류" : "신용카드"
}

order_list = []
o_sequence = 1

product_list = [{
        "seq":1,
        "name":"아메리카노",
        "price":2000,
        "option":[
            {
                "step":1,
                "menu":[
                    {"item":"HOT", "opt_price":0},
                    {"item":"ICE", "opt_price":500}
                ]
            },{
                "step":2,
                "menu":[
                    {"item":"텀블러 할인", "opt_price": -300},
                    {"item":"할인 없슴", "opt_price": 0}
                ]
            },{
                "step":3,
                "menu":[
                    {"item":"샷 추가", "opt_price": 500},
                    {"item":"추가 없슴", "opt_price": 0}
                ]
            }
        ]
    },{
        "seq":2,
        "name":"에스프레소",
        "price":2000,
        "option":[
            {
                "step":1, "menu":[
                    {"item":"HOT", "opt_price":0},
                    {"item":"ICE", "opt_price":500}
                ]
            }
        ]
    },{
        "seq":3,
        "name":"과일음료",
        "price":4000,
        "option": []
    },{
        "seq":4,
        "name":"까페라떼",
        "price":3000,
        "option": [
            {
                "step":1, "menu":[
                    {"item":"HOT", "opt_price":0},
                    {"item":"ICE", "opt_price":500}
                ]
            }
        ]
    }
]

sequence = 5


def menu_fn() :
    print("{:-^40}".format(" MENU "))
    for i, product in enumerate(product_list) :
        print(f"{i+1}. {product['name']} ({product['price']}원)")
    no = int(input("선택: "))
    while not(no>0 and no <= len(product_list) ) :
        print(f"1 ~ {len(product_list)}사이의 번호를 선택하세요.")
        no = int(input("다시 선택: "))
    return no


def order_fn() :
    global o_sequence
    print("::::::::: 메머드 커피 주문 :::::::::")
    no = menu_fn()
    idx = no -1

    order_dict = {
        "o_seq": o_sequence,  # 주문 고유 번호
        "o_name": product_list[idx]['name'],  # 주문 상품명
        "o_option" : [],
        "ea_price": product_list[idx]['price'],  # 개당 가격
        "cnt": 1  # 수량
    };
    order_list.append(order_dict)
    o_sequence += 1

    print(order_dict['o_name'], "선택.")

    # 옵션 선택
    """
    {
        "step":1, 
        "menu":[
            {"item":"HOT", "opt_price":0},
            {"item":"ICE", "opt_price":500}
        ]
    }
    """
    for opt_item in product_list[idx]['option'] :
        print(f"--------- {opt_item['step']}단계 옵션 선택")
        opt_list = opt_item['menu']
        for num, menu in enumerate( opt_list ) :
            print(f"{num+1}. {menu['item']} ({menu['opt_price']}원)")

        opt_no = int(input("선택: "))

        ppt_idx = opt_no-1
        order_dict["ea_price"] += opt_list[ppt_idx]['opt_price']
        order_dict["o_option"].append(opt_list[ppt_idx]['item'])

    # 수량 선택
    ea = int(input("수량 선택: "))
    order_dict["cnt"] = ea


def main() :
    while True :
        order_fn()
        print("------- 상품이 추가 되었습니다! ------")
        print("-------- 결제 / 추가 / 취소 ----------")
        print(">> 선택 상품")
        for i, order in enumerate(order_list):
            print(f"[{i + 1}]", order["o_name"], order["o_option"], "*", order["cnt"])

        print("1. 결제")
        print("2. 추가")
        print("3. 취소")
        no = int(input("선택: "))
        if no == 1 : break
        if no == 2 : continue
        if no == 3 :
            order_list.clear()
            return

    if len(order_list) > 0 :
        print("-----------  결제 정보 입력 ----------")
        print(">> 선택 상품: ")
        total_price = 0
        for i, order in enumerate(order_list) :
            total_price += order["ea_price"] * order["cnt"]
            print(f"[{i+1}]", order["o_name"], order["o_option"], "*", order["cnt"])

        print()
        print()
        print(">> 결제 금액: ", total_price)
        card_info["total_price"] = total_price
        card_info["카드번호"] = input("카드 번호 입력: ")
        print("--------------- 결제 완료 -----------------")
        print()

        print("^_^ 우리가 사랑하는 널 응원해~!")
        print("[영수증]")
        print("매장")
        print("교환권 번호:", 501)
        print("매머드 커피")
        print("3480401419 / 최혜원 / TEL false")
        print("주문번호: 2023002")
        current_time = datetime.now()
        print("주문일자:", current_time)
        print("=" * 40)
        print("{: <28}{: >5}".format("상품명","수량"))
        print("-" * 40)
        for order in order_list :
            print(order["o_name"])
            for opt_item in order["o_option"] :
                print("-", opt_item)

        print("=" * 40)
        print("{: <28}{: >5}".format("공급가액", card_info["total_price"]-(card_info["total_price"]/10)))
        print("{: <28}{: >5}".format("부 가 세", card_info["total_price"]/10))

        print("=" * 40)
        print("{: <28}{: >5}".format("합      계", card_info["total_price"]))
        print("{: <28}{: >5}".format("결제금액", card_info["total_price"]))

        print("=" * 40)
        for key in card_info :
            if key == "카드종류" : print(card_info[key])
            else :
                if key == "total_price" :
                    print(f"승인금액 : {card_info[key]}")
                else :
                    print(f"{key} : {card_info[key]}")

    # 재귀 호출
    print()
    print("="*40)
    main()


if __name__ == '__main__' :
    main()