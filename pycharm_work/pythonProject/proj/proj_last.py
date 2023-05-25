from tkinter import Tk, Frame, PanedWindow, ttk, messagebox
from tkinter.ttk import Labelframe, Label, Entry, Button
import tkinter.font as tkFont

from member_dao import *

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

# 이벤트 핸들러
def outputEvtHandler():
    #print("전체 보기 ...")
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

    insert((name,gra,ko,math,eng))
    global data_list
    data_list = select_all()
    refreshTreeview(data_list)

    init_entry(name, gra, ko, math, eng)


def searchEvtHandler():
    #print("검색 ...")
    sname = entry_name.get()
    if sname == "" :
        messagebox.showinfo('경고','이름을 입력 하고 검색 하세요!')
        return

    search_data_list = select(sname)

    if search_data_list == [] :
        messagebox.showinfo('경고', '찾는 정보가 없습니다!')
        return

    #print(search_data_list)
    refreshTreeview(search_data_list)

def modifyEvtHandler():
    #total = ko + math + eng
    # print("수정 ...")
    sname = entry_name.get()
    gra = entry_gra.get()
    ko = entry_ko.get()
    math = entry_math.get()
    eng = entry_eng.get()
    if sname == "" or gra == "" or ko == "" or math == "" or eng == "":
        messagebox.showinfo('알림', '이름, 학번을 모두 입력 하세요!')
        sname.focus()
        return
    print(data_list)
    idx = -1
    for i, data in enumerate(data_list) :
        try :
            idx = data.index(sname)
            if(idx != -1) :
                update((sname, gra, ko, math, eng, data[0]) )
                refreshTreeview(select_all())
                init_entry(sname, gra, ko, math, eng)
                return
        except :
            pass

    print(idx)
    if idx == -1 :
        messagebox.showinfo('경고', '찾는 정보가 없습니다!')
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


# pickle 모듈을 불러온다.
import pickle

def backupEvtHandler():
    # print("파일로 백업 ...")
    # with open('data_list.pickle', 'wb') as f:
    #     pickle.dump(data_list, f)
    pass



def loadEvtHandler():
    # print("파일로 로드 ...")
    # global data_list
    # with open('data_list.pickle', 'rb') as f:
    #     data_list = pickle.load(f)
    # refreshTreeview(data_list)
    pass

create_table()

win = Tk()
win.geometry('%dx%d+%d+%d' %(800, 600, 1100, 200))

topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100, background="#eee")

panedwindow=PanedWindow(relief="raised", bd=0)
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


# leftFrame에 Entry 위젯 추가
label_frame = Labelframe(leftFrame, text='수능... 과연 나는 서연고 갈까?')
label_frame.pack()

lbl_name = Label(label_frame, text="성명 :")
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


# bottomFrame에 Button 위젯 추가하기
panedwindow=PanedWindow(bottomFrame, relief="raised", bd=0)
panedwindow.pack()


btn_output = Button(panedwindow, text="전체보기", command=outputEvtHandler)
btn_input = Button(panedwindow, text="입력", command=inputEvtHandler)
btn_search = Button(panedwindow, text="검색", command=searchEvtHandler)
#btn_modify = Button(panedwindow, text="수정", command=modifyEvtHandler)
btn_delete = Button(panedwindow, text="삭제", command=deleteEvtHandler)
#btn_backup = Button(panedwindow, text="파일백업", command=backupEvtHandler)
#btn_load = Button(panedwindow, text="파일로드", command=loadEvtHandler)

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
#panedwindow.add(btn_modify)
panedwindow.add(btn_delete)
#panedwindow.add(btn_backup)
#panedwindow.add(btn_load)


# rightFrame에 목록 추가하기
header_list = ['no', '이름', '학번', '국어', '수학', '영어', '총점', '평균']
data_list = '''[
    (1,'kim', '101010', '25','75','14'),
    (2,'kim', '13124', '25','75','14'),
    (3,'kim', '101010', '25','75','14'),
    (4,'kim', '101010', '25','75','14'),
    (5,'kim', '101010', '25','75','14')
]'''

data_list = select_all()


tree = ttk.Treeview(rightFrame, columns=header_list, show="headings")
tree.pack()

for i, col in enumerate(header_list):
    tree.heading(col, text=col.title())
for i, item in enumerate(data_list):
    tree.insert('', 'end', iid='IID%d' %(i), values=item)

# TreeView의 각 필드 너비 설정
tree.column(0, width=30)
tree.column(1, width=50)
tree.column(2, width=60)
tree.column(3, width=80)
tree.column(4, width=80)
tree.column(5, width=80)
tree.column(6, width=80)
tree.column(7, width=80)

# TreeView의 높이 설정
tree.config(height=22)

# 앱 타이틀 라벨 추가
fontStyle = tkFont.Font(family="한양해서", size=28)
lbl_title = Label(topFrame, text="수능... 과연??? ", font=fontStyle)
lbl_title.pack(side="bottom", anchor="center")
lbl_title.place(relx=0.5, rely=0.5, anchor='center')
lbl_title.config(background="green")


# tree의 행을 클릭하면 정보가 입력 된다.
def click_item(event) :
    treeFous = tree.focus()
    treeItemValue = tree.item(treeFous).get('values')
    #print(treeItemValue)
    if len(entry_name.get()) != 0 : entry_name.delete(0,'end')
    if len(entry_gra.get()) != 0: entry_gra.delete(0, 'end')
    if len(entry_ko.get()) != 0: entry_ko.delete(0, 'end')
    if len(entry_math.get()) != 0: entry_math.delete(0, 'end')
    if len(entry_eng.get()) != 0: entry_eng.delete(0, 'end')
    #if len(entry_total.get()) != 0: entry_total.delete(0, 'end')
    #if len(entry_avg.get()) != 0: entry_avg.delete(0, 'end')
    entry_name.insert(0, treeItemValue[1])
    entry_gra.insert(0, treeItemValue[2])
    entry_ko.insert(0, treeItemValue[3])
    entry_math.insert(0, treeItemValue[4])
    entry_eng.insert(0, treeItemValue[5])
    #entry_total.insert(0, treeItemValue[6])
    #entry_avg.insert(0, treeItemValue[7])

tree.bind('<ButtonRelease-1>', click_item)


if __name__ == '__main__':
    win.mainloop()