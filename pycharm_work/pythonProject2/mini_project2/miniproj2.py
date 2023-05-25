import tkinter as tk
import random
import pygame
pygame.init()


class ClickGame:
    def __init__(self, master):
        self.master = master
        master.title("Click Game")

        self.score = 0
        self.game_over_flag = False

        self.label = tk.Label(master, text="빨간=왼클 파랑=오클",font=("나눔스퀘어 bold", 10))
        self.label.pack()

        self.score_label = tk.Label(master, text="Score: 0",font=("나눔스퀘어 bold", 20))
        self.score_label.pack()

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.target_size = 30
        self.target_color = "red"
        self.target = self.canvas.create_oval(0, 0, self.target_size, self.target_size, fill=self.target_color)
        self.move_target()

        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<Button-3>", self.right_click)
        self.canvas.bind("<Button-2>", self.game_over)

        # pygame.mixer.init()
        # pygame.mixer.music.load("Girasol - Quincas Moreira.mp3")
        # pygame.mixer.music.play(-1)

    def move_target(self):
        if not self.game_over_flag:
            x = random.randint(0, 250)
            y = random.randint(0, 250)
            self.target_color = random.choice(["red", "blue"])
            self.canvas.itemconfig(self.target, fill=self.target_color)
            self.canvas.coords(self.target, x, y, x + self.target_size, y + self.target_size)
            self.master.after(1000, self.move_target)
        else:
            self.canvas.delete(self.target)

    def left_click(self, event):
        if not self.game_over_flag:
            target_coords = self.canvas.coords(self.target)
            if self.target_color == "red" and target_coords[0] <= event.x <= target_coords[2] and target_coords[1] <= event.y <= target_coords[3]:
                self.score += 1
                self.score_label.config(text="Score: {}".format(self.score))
            else:
                self.game_over()
        else:
            self.game_over()

    def right_click(self, event):
        if not self.game_over_flag:
            target_coords = self.canvas.coords(self.target)
            if self.target_color == "blue" and target_coords[0] <= event.x <= target_coords[2] and target_coords[1] <= event.y <= target_coords[3]:
                self.score += 1
                self.score_label.config(text="Score: {}".format(self.score))
            else:
                self.game_over()
        else:
            self.game_over()

    def game_over(self):
        if not self.game_over_flag:
            self.game_over_flag = True
            target_coords = self.canvas.coords(self.target)
            if target_coords[0] == 0 and target_coords[1] == 0 and target_coords[2] == self.target_size and target_coords[3] == self.target_size:
                return

            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Button-3>")
            self.canvas.unbind("<Button-2>")

            restart_button = tk.Button(self.master, text="다시하기", command=self.restart)
            restart_button.pack()

            self.label.config(text="게임오버! 스코어: {}".format(self.score), font=("나눔스퀘어 bold", 20))

            # pygame.mixer.music.load("Small Glass Pane Shatter.mp3")
            # pygame.mixer.music.play()
    def restart(self):
        self.master.destroy()
        new_root = tk.Tk()
        new_game = ClickGame(new_root)
        new_root.mainloop()

root = tk.Tk()
my_game = ClickGame(root)
root.mainloop()