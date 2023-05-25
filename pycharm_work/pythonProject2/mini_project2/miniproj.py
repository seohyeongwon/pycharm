import tkinter
import tkinter.font
import random
import pygame

class Lotto:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title("Lotto")
        self.win.geometry("400x600")
        self.win.resizable(False, False)

        self.image_file = "lotto2.png"
        self.image = tkinter.PhotoImage(file=self.image_file)

        self.label = tkinter.Label(self.win, text="로또 번호 생성기", font=("나눔스퀘어 bold", 20), height=3)
        self.label.pack()

        self.button = tkinter.Button(self.win, height=3, command=self.click_btn,)
        self.button.config(image=self.image, width="150", height="100")
        self.button.pack()

        self.result_label = tkinter.Label(self.win,
                                          text="\n\n\n1064회 당첨번호(2023.04.22)\n\n3 6 9 18 22 35 2등 보너스14\n\n1등 총 당첨금 256억 \n\n(19명/13억)",
                                          font=("나눔스퀘어 bold", 20))
        self.result_label.pack()

        self.canvas = tkinter.Canvas(self.win, width=380, height=280)
        self.canvas.pack()

    def click_btn(self):

        self.result_label.pack_forget()


        lotto_nums_list = []
        for i in range(5):
            lotto_nums = random.sample(range(1, 46), 6)
            lotto_nums = sorted(lotto_nums)
            lotto_nums_list.append(lotto_nums)

        self.canvas.delete("all")
        self.canvas.config(width=400, height=500)

        start_x = 50
        start_y = 50
        for lotto_nums in lotto_nums_list:
            for num in lotto_nums:
                if num <= 10:
                    color = "yellow"
                elif num <= 20:
                    color = "skyblue"
                elif num <= 30:
                    color = "red"
                elif num <= 40:
                    color = "grey"
                else:
                    color = "light green"


                self.canvas.create_oval(start_x, start_y, start_x + 50, start_y + 50, fill=color,
                                        outline="black", width=2)
                self.canvas.create_text(start_x + 25, start_y + 25, text=str(num), font=("Arial", 20, "bold"))
                self.win.update()
                self.canvas.after(100)
                start_x += 50
                pygame.mixer.init()
                pygame.mixer.music.load("Wooden Bat Hits Baseball Run.mp3")
                pygame.mixer.music.play()
            self.win.update()
            self.canvas.after(200)
            start_x = 50
            start_y += 60


    def start(self):
        self.win.mainloop()


if __name__ == '__main__':
    generator = Lotto()
    generator.start()