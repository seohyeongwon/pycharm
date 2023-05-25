#from tkinter import Tk
from tkinter import Tk,Label,Button,Entry

win=Tk();

win.geometry("700x700+100+200")
win.title("window")
#win.resizable(True, True)

tlbl = Label(win, text="top>>>", background="Cyan")
tlbl.pack(side="top", fill="x")
llbl = Label(win, text="left>>>", background="Cyan")
llbl.pack(side="left", fill="x")
rlbl = Label(win, text="ri>>>", background="Cyan")
rlbl.pack(side="ri", fill="x")
blbl = Label(win, text="bo>>>", background="Cyan")
blbl.pack(side="bo", fill="x")

#lblp = Label(win, text="ph>>> ")
#lble = Label(win, text="email>>> ")

#entryn = Entry(win)
#entryp = Entry(win)
#entrye = Entry(win)

btn1 = Button(win, text="yes")
btn1.pack()
#btn2 = Button(win, text="no")

lbln.pack()
lblp.pack()
lble.pack()
btn2.pack()
btn1.pack()
entryn.pack()
entryp.pack()
entrye.pack()

#win.mainloop()

if __name__ == '__main__':
    win.mainloop();
