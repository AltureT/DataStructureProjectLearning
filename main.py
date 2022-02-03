# import tkinter
from tkinter import *
from tkinter import ttk


class App():
    def __init__(self, windowName):
        self.windowName = windowName

    def createWidgets(self):
        self.windowName.title('通讯录')
        self.windowName.geometry('600x450')

        tabs = ttk.Notebook(self.windowName, width=370, height=360)

        searchtabframe = Frame(tabs)
        self.create_search_frame(searchtabframe)

        addtabframe = Frame(tabs)
        self.create_add_frame(addtabframe)

        tabs.add(searchtabframe, text='查询')
        tabs.add(addtabframe, text='新增')
        tabs.grid(row=0, column=0)

    def create_search_frame(self, searchtabframe):
        namelabel = Label(searchtabframe, text='姓名:')
        nameentry = Entry(searchtabframe)
        searchbutton1 = Button(searchtabframe, text='查询（数组）')
        searchbutton2 = Button(searchtabframe, text='查询（链表）')
        searchbutton3 = Button(searchtabframe, text='查询（二叉树）')
        namelabel.grid(row=0, column=0, padx=10, pady=5, ipady=10)
        nameentry.grid(row=0, column=1, padx=10, pady=10, ipady=10)
        searchbutton1.grid(row=1, column=0, padx=10, pady=5, ipady=10)
        searchbutton2.grid(row=2, column=0, padx=10, pady=5, ipady=10)
        searchbutton3.grid(row=3, column=0, padx=10, pady=5, ipady=10)

    def create_add_frame(self, addtabframe):
        namelabel = Label(addtabframe, text='姓名:')
        nameentry = Entry(addtabframe)
        emaillabel = Label(addtabframe, text='邮箱:')
        emailentry = Entry(addtabframe)
        tellabel = Label(addtabframe, text='联系方式:')
        telentry = Entry(addtabframe)
        addbutton1 = Button(addtabframe, text='查询（数组）')
        addbutton2 = Button(addtabframe, text='查询（链表）')
        addbutton3 = Button(addtabframe, text='查询（二叉树）')
        namelabel.grid(row=0, column=0, padx=10, pady=5, ipady=5)
        nameentry.grid(row=0, column=1, padx=10, pady=10, ipady=5)
        emaillabel.grid(row=1, column=0, padx=10, pady=5, ipady=5)
        emailentry.grid(row=1, column=1, padx=10, pady=10, ipady=5)
        tellabel.grid(row=2, column=0, padx=10, pady=5, ipady=5)
        telentry.grid(row=2, column=1, padx=10, pady=10, ipady=5)
        addbutton1.grid(row=3, column=0, padx=10, pady=5, ipady=10)
        addbutton2.grid(row=4, column=0, padx=10, pady=5, ipady=10)
        addbutton3.grid(row=5, column=0, padx=10, pady=5, ipady=10)


def main_app():
    window = Tk()
    app = App(window)
    app.createWidgets()
    window.mainloop()


if __name__ == '__main__':
    main_app()
