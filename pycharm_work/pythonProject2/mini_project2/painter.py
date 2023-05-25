import tkinter
import random
from tkinter import *
from pygame import mixer

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.master.title("그림판")
        self.master.geometry("640x500")

        self.color = "black"
        self.brush_size = 2
        self.brush_shape = "circle"

        # 이전 마우스 위치를 저장할 목록 만들기
        self.prev_x = None
        self.prev_y = None

        self.create_widgets()


    def create_widgets(self):
        self.canvas = Canvas(self.master, bg="white", width=640, height=420)
        self.canvas.pack()

        # 마우스 이벤트 바인딩
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset_prev_pos)
        self.canvas.bind("<Button-3>", self.toggle_color) #지우개 모드

        color_frame = Frame(self.master)
        color_frame.pack(side=BOTTOM,pady=2)

        colors = ["black", "red", "green", "blue", "yellow", "orange", "purple"]

        for color in colors:
            Button(color_frame, bg=color, width=3, height=1, command=lambda c=color: self.set_color(c)).pack(side=LEFT)

        size_frame = Frame(self.master)
        size_frame.pack(side=BOTTOM)

        eraser = Label(self.master, text=f"우클릭 시 지우개모드 전환")
        eraser.pack(side=LEFT,anchor="sw")

        clear_btn = Button(self.master, text="초기화", command=self.clear)
        clear_btn.pack(side=RIGHT, padx=5, pady=2)

        size_label = Label(size_frame, text="Size:")
        size_label.pack(side=LEFT)

        size_btn_small = Button(size_frame, text="작게", width=5, command=lambda: self.set_brush_size(2))
        size_btn_small.pack(side=LEFT)

        size_btn_medium = Button(size_frame, text="중간", width=5, command=lambda: self.set_brush_size(5))
        size_btn_medium.pack(side=LEFT)

        size_btn_large = Button(size_frame, text="크게", width=5, command=lambda: self.set_brush_size(10))
        size_btn_large.pack(side=LEFT)



    def draw(self, event):
        if self.prev_x and self.prev_y:
            # 이전 위치와 현재 위치의 평균 계산
            x = (event.x + self.prev_x) // 2
            y = (event.y + self.prev_y) // 2

            # 브러시 모양 그리기
            if self.brush_shape == "circle":
                self.canvas.create_oval(x - self.brush_size, y - self.brush_size, x + self.brush_size, y + self.brush_size,
                                         fill=self.color, outline=self.color)
            elif self.brush_shape == "square":
                self.canvas.create_rectangle(x - self.brush_size, y - self.brush_size, x + self.brush_size, y + self.brush_size,
                                         fill=self.color, outline=self.color)

        # 이전 마우스 위치 업데이트
        self.prev_x = event.x
        self.prev_y = event.y

    def reset_prev_pos(self, event):
        # 이전 마우스 위치 재설정
        self.prev_x = None
        self.prev_y = None

    def set_color(self, color):
        self.color = color

    def toggle_color(self, event): # 지우개
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def set_brush_size(self, size):
        self.brush_size = size

    def set_brush_shape(self, shape):
        self.brush_shape = shape

    def clear(self):
        self.canvas.delete("all")


def start_paint_app():
    root = Tk()
    PaintApp(root)
    root.mainloop()





if __name__ == '__main__':
    start_paint_app()


