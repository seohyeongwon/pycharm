from tkinter import Tk
from tkinter.ttk import Label,Button

win=Tk();

win.geometry("700x700+100+200")
win.title("window")
win.resizable(True, True)

lbl = Label(win, text="res>>> ");
btn1 = Button(win, text="yes")
btn2 = Button(win, text="no")

lbl.pack()
btn2.pack()
btn1.pack()

#win.mainloop()

if __name__ == '__main__':
    win.mainloop();
