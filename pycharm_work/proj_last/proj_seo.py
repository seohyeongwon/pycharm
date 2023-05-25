import tkinter
from tkinter import Tk, Frame, PanedWindow, ttk, messagebox, PhotoImage
from tkinter.ttk import Labelframe, Label, Entry, Button
import tkinter.font as tkFont

from member_dao import *

from tkinter import *


def init_entry(name, gra, ko, math, eng) :
    entry_name.delete(0, len(name))
    entry_gra.delete(0, len(gra))
    entry_ko.delete(0, len(ko))
    entry_math.delete(0, len(math))
    entry_eng.delete(0, len(eng))

def deleteTreeData() :
    children = tree.get_children()
    if children != '()':
        for item in children:
            tree.delete(item)

def refreshTreeData(data_list) :
    for i, item in enumerate(data_list):
        tree.insert('', 'end', iid='IID%d' % (i), values=item)

def refreshTreeview(data_list) :
    deleteTreeData()
    refreshTreeData(data_list)


def outputEvtHandler():
    global data_list
    data_list = select_all()
    refreshTreeview(data_list)

def inputEvtHandler():
    name = entry_name.get()
    gra = entry_gra.get()
    ko = entry_ko.get()
    math = entry_math.get()
    eng = entry_eng.get()

    if name=="" or gra==""or ko==""or math==""or eng=="":
        messagebox.showinfo('알림', '이름, 학번, 국어, 수학, 영어 입력 해야 뭐가 나오지!!!!!')
        return

    total = int(ko) + int(math) + int(eng)
    avg = round(float(total) // 3.0,3)

    sch = "서울대" if float(avg) >= 95 else (
        "연고대" if float(avg) >= 85 else ("한성" if float(avg) >= 75 else ("중경" if float(avg) >= 65 else ("건홍부경" if float(avg) >= 55 else "대학 X or 재수"))))

    insert((name, gra, ko, math, eng, total, avg, sch))
    global data_list
    data_list = select_all()
    refreshTreeview(data_list)

    init_entry(name, gra, ko, math, eng)


def searchEvtHandler():
    sname = entry_name.get()
    if sname == "" :
        messagebox.showinfo('경고','이름을 입력 하고 검색 하세요!')
        return

    search_data_list = select(sname)

    if search_data_list == [] :
        messagebox.showinfo('경고', '찾는 정보가 없습니다!')
        return

    refreshTreeview(search_data_list)

def modifyEvtHandler():
    pass

def deleteEvtHandler():
    #print("삭제 ...")
    sname = entry_name.get()
    if sname == "":
        messagebox.showinfo('경고', '이름을 입력 하고 검색 하세요!')
        return

    idx = -1
    for data in data_list:
        try:
            idx = data.index(sname)
            delete(data[0])
            refreshTreeview(select_all())
            init_entry(sname,"","")
            return
        except:
            pass

    if idx == -1 :
        messagebox.showinfo('경고', '찾는 정보가 없습니다!')


import pickle

def backupEvtHandler():
    pass

def loadEvtHandler():
    pass

create_table()

win = Tk()
win.geometry('%dx%d+%d+%d' %(900, 600, 500, 70))
win.title("서연고 가고싶니?")

topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100, background="#eee")

panedwindow = PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(win)
leftFrame.pack(side='left')
leftFrame.config(width=500, height=800, background="#eee")

rightFrame = Frame(win)
rightFrame.pack(side='right')
rightFrame.config(width=600, height=470, background="green")

panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

bottomFrame = Frame(win)
bottomFrame.pack(side='bottom')
bottomFrame.config(width=800, height=30, background="blue")


label_frame = Labelframe(leftFrame, text='과연???')
label_frame.pack()

lbl_name = Label(label_frame, text="이름 :")
lbl_gra = Label(label_frame, text="학번 :")
lbl_ko = Label(label_frame, text="국어 :")
lbl_math = Label(label_frame, text="수학 :")
lbl_eng = Label(label_frame, text="영어 :")

entry_name = Entry(label_frame)
entry_gra = Entry(label_frame)
entry_ko = Entry(label_frame)
entry_math = Entry(label_frame)
entry_eng = Entry(label_frame)

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1, padx=5, pady=5)
lbl_gra.grid(row=1, column=0)
entry_gra.grid(row=1, column=1, padx=5, pady=5)
lbl_ko.grid(row=2, column=0)
entry_ko.grid(row=2, column=1, padx=5, pady=5)
lbl_math.grid(row=3, column=0)
entry_math.grid(row=3, column=1, padx=5, pady=5)
lbl_eng.grid(row=4, column=0)
entry_eng.grid(row=4, column=1, padx=5, pady=5)


panedwindow=PanedWindow(bottomFrame, relief="raised", bd=0)
panedwindow.pack()

btn_output = Button(panedwindow, text="돌아가기", command=outputEvtHandler)
btn_input = Button(panedwindow, text="입력", command=inputEvtHandler)
btn_search = Button(panedwindow, text="검색", command=searchEvtHandler)
btn_delete = Button(panedwindow, text="삭제", command=deleteEvtHandler)

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_delete)


header_list = ['no', '이름', '학번', '국어', '수학', '영어', '총점', '평균', '대학']
data_list = '''[
    {1,"kim", 101010, 100, 100, 100, 0, 0.0, "서울대"}
]'''

data_list = select_all()


tree = ttk.Treeview(rightFrame, columns=header_list, show="headings")
tree.pack()

for i, col in enumerate(header_list):
    tree.heading(col, text=col.title())
for i, item in enumerate(data_list):
    tree.insert('', 'end', iid='IID%d' %(i), values=item)


tree.column(0, width=30)
tree.column(1, width=80)
tree.column(2, width=70)
tree.column(3, width=60)
tree.column(4, width=60)
tree.column(5, width=60)
tree.column(6, width=80)
tree.column(7, width=80)
tree.column(8, width=100)

tree.config(height=22)

fontStyle = tkFont.Font(family="한양해서", size=28)
lbl_title = Label(topFrame, text="과연 나는 서연고 갈 수 있을까???", font=fontStyle)
lbl_title.pack(side="bottom", anchor="center")
lbl_title.place(relx=0.5, rely=0.5, anchor='center')
lbl_title.config(background="green")


def click_item(event) :
    treeFous = tree.focus()
    treeItemValue = tree.item(treeFous).get('values')
    #print(treeItemValue)
    if len(entry_name.get()) != 0 : entry_name.delete(0,'end')
    if len(entry_gra.get()) != 0: entry_gra.delete(0, 'end')
    if len(entry_ko.get()) != 0: entry_ko.delete(0, 'end')
    if len(entry_math.get()) != 0: entry_math.delete(0, 'end')
    if len(entry_eng.get()) != 0: entry_eng.delete(0, 'end')
    entry_name.insert(0, treeItemValue[1])
    entry_gra.insert(0, treeItemValue[2])
    entry_ko.insert(0, treeItemValue[3])
    entry_math.insert(0, treeItemValue[4])
    entry_eng.insert(0, treeItemValue[5])

tree.bind('<ButtonRelease-1>', click_item)


if __name__ == '__main__':
    win.mainloop()