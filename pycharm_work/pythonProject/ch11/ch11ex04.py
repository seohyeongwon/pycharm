from tkinter import Tk
from tkinter.ttk import Label,Button,Entry

win=Tk();

win.geometry("700x700+100+200")
win.title("window")
#win.resizable(True, True)

lbln = Label(win, text="name>>> ")
lblp = Label(win, text="ph>>> ")
lble = Label(win, text="email>>> ")

entryn = Entry(win)
entryp = Entry(win)
entrye = Entry(win)

btn1 = Button(win, text="yes")
btn2 = Button(win, text="no")

lbln.pack()
entryn.pack()
lblp.pack()
entryp.pack()
lble.pack()
entrye.pack()

btn1.pack()
btn2.pack()

#win.mainloop()

if __name__ == '__main__':
    win.mainloop();
