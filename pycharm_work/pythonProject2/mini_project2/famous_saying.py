quotes = ["당신이 원하는 것이 어떤 것이든지,\n그것을 이룰 방법을 이미 다른 사람들이 발견해냈다는 것을 기억하라.",
"성공은 당신이 넘어졌을 때 일어나는 것이 아니라,\n얼마나 많이 일어나느냐에 달려있다.",
"당신이 꿈꾸는 일을 한다는 것은 절대 쉽지 않을 것이다.\n그러나 그 일을 한다면 인생에서 최고의 경험 중 하나가 될 것이다.",
"시작할 때 완벽하게 할 필요는 없다.\n시작하고 나서 완벽하게 만들면 된다. ",
"당신이 가진 능력은 당신이 가진 열정에 비례한다. ",
"프로그래밍은 마법과 같다. 어떤 것이든 할 수 있다. ",
"지금까지 내가 발견한 가장 중요한 것은,\n사람들이 어떻게 일하는가가 아니라, 왜 일하는가이다.",
"성공의 비밀은 자신이 하는 일을 사랑하는 것이다.",
"프로그래밍은 예술이 아니다. 그것은 단순히 무엇인가를 만드는 기술이다.",
"오늘을 열심히 살아가면 내일은 자연스럽게 따라온다."]
meanings = ["- Tony Robbins -",
           "- Vince Lombardi -",
           "- Steve Jobs -",
           "- Elie Tahari -",
           "- Zig Ziglar -",
           "- Karolina Szczur -",
           "- Simon Sinek -",
           "- Steve Jobs -",
           "- John Romero -",
           "- Joe Polish -"]

from tkinter import *
import random

from pygame import mixer

filename = 'fs_main.mp3'
mixer.init()
mixer.music.load(filename)
mixer.music.play(-1)

def click_btn():
    # 명언과 의미 리스트에서 랜덤한 인덱스 선택
    random_quote = random.randint(0, len(quotes)-1)
    # 선택된 명언과 해당 명언의 의미 텍스트를 캔버스에 출력
    canvas.itemconfig(kor, text=quotes[random_quote])
    canvas.itemconfig(person, text=meanings[random_quote])

# 윈도우 설정
window = Tk()
window.title("오늘의 명언")
window.geometry("700x500+400+100")
window.resizable(False,False)

# 캔버스 생성 및 배치
canvas = Canvas(window, width=700, height=500, bg="pink")
canvas.pack()

# 이미지 삽입
img = PhotoImage(file="fs_main.png")
canvas.create_image(350,250, image=img)

# 명언 및 의미 출력용 텍스트 생성
kor = canvas.create_text(350, 180, text="개발자를 위한 오늘의 명언", fill="white", font=("나눔바른펜", 16, "bold"), anchor="center")
person = canvas.create_text(550, 250, text="", fill="white", font=("나눔바른펜", 20, "bold"), anchor="center")

# 버튼 생성 및 배치
button = Button(window, text="명언 보기", font=("나눔바른펜", 20, "bold"), highlightthickness=0, bd=0, command=click_btn)
button.place(x=285 , y=400)

window.mainloop()
