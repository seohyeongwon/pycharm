# 필요한 모듈 import
import tkinter
import tkinter as tk
from tkinter import *
from pygame import mixer
import pygame
import os
import matplotlib as mat
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

mat.rcParams['font.family']='Gulim'
# 창 생성
root = Tk()
root.geometry("1600x850+150+50")
root.title("놀고 먹고 코딩하고")

# 팀 제목
lbl = Label(root,text="놀고 먹고 코딩하고",font=("Gulim", 25, "bold"))
lbl.place(x=250, y=10)

# 프레임 생성
button_frame = Frame(root)
button_frame.place(x=50, y=70)

# 그림판 버튼 생성
def open_draw():
    os.system('painter.py')

draw_btn = Button(button_frame, text="그림판 열기", command=open_draw)
draw_btn.grid(row=0, column=0, padx=10, pady=10)
image_file1 = "painter.png"
image1 = tkinter.PhotoImage(file=image_file1)
draw_btn.config(image=image1, width="700", height="80")
draw_btn2 = Button(button_frame, text="통계 보기", command=lambda: show_graph(root))
draw_btn2.grid(row=0, column=1, padx=10, pady=10)

main_title = Label(text="메인이미지")
main_title.place(x=880,y=90)
image_city = "city.png"
image_city1 = tkinter.PhotoImage(file=image_city)
main_title.config(image=image_city1, width="700", height="200")


# 그림판 그래프를 표시하는 함수
def show_graph(master):
    fig, ax = plt.subplots()

    fruits = ['좋아요', '싫어요', '구독자', '조회수']
    counts = [150, 2, 160, 180]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_title('그림판')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().place(x=900,y=330)
# 오늘의 명언 버튼 생성
def open_quote():
    os.system('famous_saying.py')

quote_btn = Button(button_frame, text="오늘의 명언 보기", command=open_quote)
quote_btn.grid(row=1, column=0, padx=10, pady=10)
image_file2 = "junwon_title.png"
image2 = tkinter.PhotoImage(file=image_file2)
quote_btn.config(image=image2, width="700", height="80")

quote_btn2 = Button(button_frame, text="통계 보기", command=lambda: show_quote(root))
quote_btn2.grid(row=1, column=1, padx=10, pady=10)

# 명언 그래프를 표시하는 함수
def show_quote(master):
    fig, ax = plt.subplots()

    fruits = ['좋아요', '싫어요', '구독자', '조회수']
    counts = [210, 3, 60, 230]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_title('오늘의 명언')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().place(x=900,y=330)

# 로또 번호 버튼 생성
def open_lotto():
    os.system('miniproj.py')

lotto_btn = Button(button_frame, text="로또 번호 생성기", command=open_lotto)
lotto_btn.grid(row=2, column=0, padx=10, pady=10)
image_file3 = "lottobanner.png"
image3 = tkinter.PhotoImage(file=image_file3)
lotto_btn.config(image=image3, width="700", height="80")
lotto_btn2 = Button(button_frame, text="통계 보기", command=lambda: show_lotto(root))
lotto_btn2.grid(row=2, column=1, padx=10, pady=10)

# 로또 그래프를 표시하는 함수
def show_lotto(master):
    fig, ax = plt.subplots()

    fruits = ['좋아요', '싫어요', '구독자', '조회수']
    counts = [400, 2, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_title('로또')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().place(x=900,y=330)

# 클릭 게임 버튼 생성
def open_click_game():
    os.system('miniproj2.py')

game_btn = Button(button_frame, text="클릭 게임", command=open_click_game)
game_btn.grid(row=3, column=0, padx=10, pady=10)
image_file4 = "click_game.png"
image4 = tkinter.PhotoImage(file=image_file4)
game_btn.config(image=image4, width="700", height="80")
game_btn2 = Button(button_frame, text="통계 보기", command=lambda: show_click_game(root))
game_btn2.grid(row=3, column=1, padx=10, pady=10)

# 클릭게임 그래프를 표시하는 함수
def show_click_game(master):
    fig, ax = plt.subplots()

    fruits = ['좋아요', '싫어요', '구독자', '조회수']
    counts = [200, 4, 30, 600]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_title('클릭 게임')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().place(x=900,y=330)

# 서연고 버튼 생성
def open_seo():
    os.system('project_seo.py')

seo_btn = Button(button_frame, text="서연고", command=open_seo)
seo_btn.grid(row=4, column=0, padx=10, pady=10)
image_file5 = "seoyongo.png"
image5 = tkinter.PhotoImage(file=image_file5)
seo_btn.config(image=image5, width="700", height="80")
seo_btn2 = Button(button_frame, text="통계 보기", command=lambda: show_seo(root))
seo_btn2.grid(row=4, column=1, padx=10, pady=10)

# 서연고 그래프를 표시하는 함수
def show_seo(master):
    fig, ax = plt.subplots()

    fruits = ['좋아요', '싫어요', '구독자', '조회수']
    counts = [200, 4, 30, 400]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_title('서연고 가기')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().place(x=900,y=330)

# 텍스트 게임 버튼 생성
def open_txtgame():
    os.system('text_game.py')

txt_game_btn = Button(button_frame, text="텍스트 게임", command=open_txtgame)
txt_game_btn.grid(row=5, column=0, padx=10, pady=10)
image_file6 = "text_game.png"
image6 = tkinter.PhotoImage(file=image_file6)
txt_game_btn.config(image=image6, width="700", height="80")
txt_game_btn2 = Button(button_frame, text="통계 보기", command=lambda: show_txtgame(root))
txt_game_btn2.grid(row=5, column=1, padx=10, pady=10)

# 서연고 그래프를 표시하는 함수
def show_txtgame(master):
    fig, ax = plt.subplots()

    fruits = ['좋아요', '싫어요', '구독자', '조회수']
    counts = [120, 6, 40, 350]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_title('텍스트 게임')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().place(x=900,y=330)

# 애벌레 키우기 게임 버튼 생성
def open_catterpillar_game():
    os.system('pygame_snake2.py')

cp_game_btn = Button(button_frame, text="애벌레 키우기 게임", command=open_catterpillar_game)
cp_game_btn.grid(row=6, column=0, padx=10, pady=10)
image_file7 = "catterpillar.png"
image7 = tkinter.PhotoImage(file=image_file7)
cp_game_btn.config(image=image7, width="700", height="80")
cp_game_btn2 = Button(button_frame, text="통계 보기", command=lambda: show_cp_game(root))
cp_game_btn2.grid(row=6, column=1, padx=10, pady=10)

# 서연고 그래프를 표시하는 함수
def show_cp_game(master):
    fig, ax = plt.subplots()

    fruits = ['좋아요', '싫어요', '구독자', '조회수']
    counts = [150, 4, 60, 200]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_title('애벌레 키우기 게임')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().place(x=900,y=330)

# 창 실행
root.mainloop()
