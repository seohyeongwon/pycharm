import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=386
        height=741
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_90=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_90["font"] = ft
        GLabel_90["fg"] = "#333333"
        GLabel_90["justify"] = "center"
        GLabel_90["text"] = "성적 입력"
        GLabel_90.place(x=20,y=20,width=214,height=87)

        GLabel_155=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_155["font"] = ft
        GLabel_155["fg"] = "#333333"
        GLabel_155["justify"] = "center"
        GLabel_155["text"] = "국어"
        GLabel_155.place(x=20,y=120,width=70,height=25)

        GLabel_27=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_27["font"] = ft
        GLabel_27["fg"] = "#333333"
        GLabel_27["justify"] = "center"
        GLabel_27["text"] = "수학"
        GLabel_27.place(x=100,y=120,width=70,height=25)

        GLabel_883=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_883["font"] = ft
        GLabel_883["fg"] = "#333333"
        GLabel_883["justify"] = "center"
        GLabel_883["text"] = "영어"
        GLabel_883.place(x=180,y=120,width=70,height=25)

        GButton_505 = tk.Button(root)
        GButton_505["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_505["font"] = ft
        GButton_505["fg"] = "#000000"
        GButton_505["justify"] = "center"
        GButton_505["text"] = "눌러봐"
        GButton_505.place(x=290, y=150, width=70, height=25)
        GButton_505["command"] = self.GButton_505_command

        GLabel_827=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "총점"
        GLabel_827.place(x=20,y=190,width=70,height=25)

        GLabel_130=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_130["font"] = ft
        GLabel_130["fg"] = "#333333"
        GLabel_130["justify"] = "center"
        GLabel_130["text"] = "평균"
        GLabel_130.place(x=170,y=190,width=70,height=25)

        GLabel_866=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_866["font"] = ft
        GLabel_866["fg"] = "#333333"
        GLabel_866["justify"] = "center"
        GLabel_866["text"] = "서연고 갈지... 못 갈지..."
        GLabel_866.place(x=10,y=230,width=254,height=30)



        GLineEdit_738=tk.Entry(root)
        GLineEdit_738["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_738["font"] = ft
        GLineEdit_738["fg"] = "#333333"
        GLineEdit_738["justify"] = "center"
        GLineEdit_738["text"] = "국"
        GLineEdit_738.place(x=30,y=150,width=70,height=25)

        GLineEdit_890=tk.Entry(root)
        GLineEdit_890["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_890["font"] = ft
        GLineEdit_890["fg"] = "#333333"
        GLineEdit_890["justify"] = "center"
        GLineEdit_890["text"] = "수"
        GLineEdit_890.place(x=110,y=150,width=70,height=25)

        GLineEdit_129=tk.Entry(root)
        GLineEdit_129["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_129["font"] = ft
        GLineEdit_129["fg"] = "#333333"
        GLineEdit_129["justify"] = "center"
        GLineEdit_129["text"] = "영"
        GLineEdit_129.place(x=190,y=150,width=70,height=25)

        GLineEdit_426=tk.Entry(root)
        GLineEdit_426["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_426["font"] = ft
        GLineEdit_426["fg"] = "#333333"
        GLineEdit_426["justify"] = "center"
        GLineEdit_426["text"] = "총점"
        GLineEdit_426.place(x=90,y=190,width=70,height=25)

        GLineEdit_642=tk.Entry(root)
        GLineEdit_642["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_642["font"] = ft
        GLineEdit_642["fg"] = "#333333"
        GLineEdit_642["justify"] = "center"
        GLineEdit_642["text"] = "평균"
        GLineEdit_642.place(x=240,y=190,width=70,height=25)

        GLineEdit_730=tk.Entry(root)
        GLineEdit_730["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_730["font"] = ft
        GLineEdit_730["fg"] = "#333333"
        GLineEdit_730["justify"] = "center"
        GLineEdit_730["text"] = "합 / 불"
        GLineEdit_730.place(x=30,y=270,width=70,height=25)



        GLabel_610=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_610["font"] = ft
        GLabel_610["fg"] = "#333333"
        GLabel_610["justify"] = "center"
        GLabel_610["text"] = "명단"
        GLabel_610.place(x=20,y=320,width=70,height=25)

        GLabel_42=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_42["font"] = ft
        GLabel_42["fg"] = "#333333"
        GLabel_42["justify"] = "center"
        GLabel_42["text"] = "seo"
        GLabel_42.place(x=20,y=360,width=70,height=25)

        GLabel_50=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_50["font"] = ft
        GLabel_50["fg"] = "#333333"
        GLabel_50["justify"] = "center"
        GLabel_50["text"] = "합"
        GLabel_50.place(x=110,y=360,width=70,height=25)

        GLabel_841=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_841["font"] = ft
        GLabel_841["fg"] = "#333333"
        GLabel_841["justify"] = "center"
        GLabel_841["text"] = "kim"
        GLabel_841.place(x=20,y=400,width=70,height=25)

        GLabel_89=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_89["font"] = ft
        GLabel_89["fg"] = "#333333"
        GLabel_89["justify"] = "center"
        GLabel_89["text"] = "불"
        GLabel_89.place(x=110,y=400,width=70,height=25)

        GLabel_314=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_314["font"] = ft
        GLabel_314["fg"] = "#333333"
        GLabel_314["justify"] = "center"
        GLabel_314["text"] = "park"
        GLabel_314.place(x=20,y=440,width=70,height=25)

        GLabel_26=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_26["font"] = ft
        GLabel_26["fg"] = "#333333"
        GLabel_26["justify"] = "center"
        GLabel_26["text"] = "불"
        GLabel_26.place(x=110,y=440,width=70,height=25)

        GLabel_234=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_234["font"] = ft
        GLabel_234["fg"] = "#333333"
        GLabel_234["justify"] = "center"
        GLabel_234["text"] = "lee"
        GLabel_234.place(x=20,y=480,width=70,height=25)

        GLabel_546=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_546["font"] = ft
        GLabel_546["fg"] = "#333333"
        GLabel_546["justify"] = "center"
        GLabel_546["text"] = "불"
        GLabel_546.place(x=110,y=480,width=70,height=25)

        GLabel_932=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_932["font"] = ft
        GLabel_932["fg"] = "#333333"
        GLabel_932["justify"] = "center"
        GLabel_932["text"] = "chol"
        GLabel_932.place(x=20,y=520,width=70,height=25)

        GLabel_377=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#333333"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "불"
        GLabel_377.place(x=110,y=520,width=70,height=25)

    def GButton_505_command(self):
        print("command")


class CCCC :
    def __init__(self, GLabel_155, GLabel_27, GLabel_883):
        self.GLbel_155 = GLabel_155
        self.GLbel_27 = GLabel_27
        self.GLbel_883 = GLabel_883
        self.GLineEdit_426 = self.GLbel_155 + self.GLbel_27 + self.GLbel_883
        self.GLineEdit_642 = round(self.GLineEdit_426/3, 3)

    def GLbel_155(self):
        pass

    def GLbel_27(self):
        pass

    def GLbel_883(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
