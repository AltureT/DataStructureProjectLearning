# import tkinter
from tkinter import *
from tkinter import ttk


class App():
    def __init__(self, windowName):
        self.windowName = windowName

    def createWidgets(self):
        self.windowName.title('通讯录')
        self.windowName.geometry('630x430')

        tabs = ttk.Notebook(self.windowName, width=370, height=360)

        searchtabframe = Frame(tabs)
        self.create_search_frame(searchtabframe)

        addtabframe = Frame(tabs)
        self.create_add_frame(addtabframe)

        self.log_system()

        tabs.add(searchtabframe, text='查询')
        tabs.add(addtabframe, text='新增')
        tabs.grid(row=0, column=0, rowspan=24, columnspan=2)

    def create_search_frame(self, searchtabframe):
        namelabel = Label(searchtabframe, text='姓名:')
        name = StringVar()
        nameentry = Entry(searchtabframe, textvariable=name)

        searchbutton1 = Button(searchtabframe, text='查询（数组）')
        searchbutton2 = Button(searchtabframe, text='查询（链表）')
        searchbutton3 = Button(searchtabframe, text='查询（二叉树）')

        namelabel.grid(row=0, column=0, padx=10, pady=5, ipady=10)
        nameentry.grid(row=0, column=1, padx=10, pady=10, ipady=10)
        searchbutton1.grid(row=1, column=0, padx=10, pady=5, ipady=10)
        searchbutton2.grid(row=2, column=0, padx=10, pady=5, ipady=10)
        searchbutton3.grid(row=3, column=0, padx=10, pady=5, ipady=10)

        result = StringVar()
        resultentry = Entry(searchtabframe, textvariable=result)
        resultentry['state'] = 'readonly'
        resultentry.grid(row=1, column=1, rowspan=3, padx=10, pady=5, ipady=40)

    def create_add_frame(self, addtabframe):
        namelabel = Label(addtabframe, text='姓名:')
        name = StringVar()
        nameentry = Entry(addtabframe, textvariable=name)

        emaillabel = Label(addtabframe, text='邮箱:')
        email = StringVar()
        emailentry = Entry(addtabframe, textvariable=email)

        tellabel = Label(addtabframe, text='联系方式:')
        tel = StringVar()
        telentry = Entry(addtabframe, textvariable=tel)

        addbutton1 = Button(addtabframe, text='新增（数组）')
        addbutton2 = Button(addtabframe, text='新增（链表）')
        addbutton3 = Button(addtabframe, text='新增（二叉树）')

        namelabel.grid(row=0, column=0, padx=10, pady=5, ipady=5)
        nameentry.grid(row=0, column=1, padx=10, pady=10, ipady=5)
        emaillabel.grid(row=1, column=0, padx=10, pady=5, ipady=5)
        emailentry.grid(row=1, column=1, padx=10, pady=10, ipady=5)
        tellabel.grid(row=2, column=0, padx=10, pady=5, ipady=5)
        telentry.grid(row=2, column=1, padx=10, pady=10, ipady=5)
        addbutton1.grid(row=3, column=0, padx=10, pady=5, ipady=10)
        addbutton2.grid(row=4, column=0, padx=10, pady=5, ipady=10)
        addbutton3.grid(row=5, column=0, padx=10, pady=5, ipady=10)

        result = StringVar()
        resultentry = Entry(addtabframe, textvariable=result)
        resultentry['state'] = 'readonly'
        resultentry.grid(row=3, column=1, rowspan=3, padx=10, pady=5, ipady=40)

    def log_system(self):
        namelabel = Label(self.windowName, text='操作日志')
        namelabel.grid(row=0, column=2)
        result = StringVar()
        resultentry = Entry(self.windowName, textvariable=result)
        resultentry['state'] = 'readonly'
        resultentry.grid(row=1, column=2, ipady=50)


def main_app():
    window = Tk()
    app = App(window)
    app.createWidgets()
    window.mainloop()


if __name__ == '__main__':
    main_app()
