import tkinter as tk
import os
import pygame
from tkVideoPlayer import TkinterVideo


pygame.mixer.init()
pygame.mixer.music.load("banner_final.mp3")
pygame.mixer.music.play()

root = tk.Tk()
root.geometry("1920x900+0+50")

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"banner_final.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video
# 그림판 버튼 생성
def open_main():
    os.system('main.py')


def open_new_window():
    # 이전 창 닫기
    pygame.mixer.music.stop()
    root.destroy()
    open_main()

# 버튼 생성
button = tk.Button(root, text="스킵하기", command=open_new_window)
button.pack()
root.after(17000,open_new_window)
root.mainloop()