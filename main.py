# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import global_val
import solution


class App:
    def __init__(self, windowName):
        self.sresult = Text()
        self.aresult = Text()
        self.logresult = Text()
        self.windowName = windowName
        global_val.init()
        self.create_widgets()
        print(id(self.sresult))

    def create_widgets(self):
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
        nameentry = Entry(searchtabframe)
        self.sresult = Text(searchtabframe)

        searchbutton1 = Button(searchtabframe, text='查询（数组）',
                               command=lambda: self.exec_and_output(0, [nameentry.get()]))
        searchbutton2 = Button(searchtabframe, text='查询（链表）',
                               command=lambda: self.exec_and_output(0, [nameentry.get()]))
        searchbutton3 = Button(searchtabframe, text='查询（二叉树）',
                               command=lambda: self.exec_and_output(0, [nameentry.get()]))
        print(searchbutton1)
        namelabel.grid(row=0, column=0, padx=10, pady=5, ipady=10)
        nameentry.grid(row=0, column=1, padx=10, pady=10, ipady=10)
        searchbutton1.grid(row=1, column=0, padx=10, pady=5, ipady=10)
        searchbutton2.grid(row=2, column=0, padx=10, pady=5, ipady=10)
        searchbutton3.grid(row=3, column=0, padx=10, pady=5, ipady=10)

        self.sresult['width'] = 25
        self.sresult['height'] = 10
        self.sresult.grid(row=1, column=1, rowspan=3, columnspan=1)

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

        addbutton1 = Button(addtabframe, text='新增（数组）',
                            command=lambda: self.exec_and_output(0,
                                                                 [nameentry.get(), emailentry.get(), telentry.get()]))
        addbutton2 = Button(addtabframe, text='新增（链表）',
                            command=lambda: self.exec_and_output(0,
                                                                 [nameentry.get(), emailentry.get(), telentry.get()]))
        addbutton3 = Button(addtabframe, text='新增（二叉树）',
                            command=lambda: self.exec_and_output(0,
                                                                 [nameentry.get(), emailentry.get(), telentry.get()]))

        namelabel.grid(row=0, column=0, padx=10, pady=5, ipady=5)
        nameentry.grid(row=0, column=1, padx=10, pady=10, ipady=5)
        emaillabel.grid(row=1, column=0, padx=10, pady=5, ipady=5)
        emailentry.grid(row=1, column=1, padx=10, pady=10, ipady=5)
        tellabel.grid(row=2, column=0, padx=10, pady=5, ipady=5)
        telentry.grid(row=2, column=1, padx=10, pady=10, ipady=5)
        addbutton1.grid(row=3, column=0, padx=10, pady=5, ipady=10)
        addbutton2.grid(row=4, column=0, padx=10, pady=5, ipady=10)
        addbutton3.grid(row=5, column=0, padx=10, pady=5, ipady=10)

        self.aresult = Text(addtabframe)
        self.aresult['width'] = 25
        self.aresult['height'] = 10
        self.aresult.grid(row=3, column=1, rowspan=3, columnspan=1)

    def log_system(self):
        namelabel = Label(self.windowName, text='操作日志')
        namelabel.grid(row=0, column=2)
        self.logresult = Text(self.windowName)
        self.logresult['width'] = 25
        self.logresult['height'] = 30
        self.logresult.grid(row=1, column=2)

    def exec_and_output(self, code: int, info: list):
        """
        执行查找/新增，并做输出处理
        :param code: 0代表查找，1代表新增
        :param info: [name,email,tel]
        :return:
        """
        print(id(self.sresult))
        if code == 0:
            name = self.from_array(info[0])
            self.sresult.delete(1.0, 'end')
            s = global_val.get_user_info().get_user_name() + '\n' + \
                global_val.get_user_info().get_user_email() + '\n' + \
                global_val.get_user_info().get_user_tel()
            self.sresult.insert(1.0, s)
            self.sresult.insert(1.0, name)

    def from_array(self, name):
        print(name)
        solution.array_find(name)

        return name

    def from_link(self, name):
        pos = 3
        return pos

    def from_tree(self, name):
        pos = 3
        return pos

    def add_to_array(self, name, email, tel):
        pos = 3
        return pos

    def add_to_link(self, name, email, tel):
        pos = 3
        return pos

    def add_to_tree(self, name, email, tel):
        pos = 3
        return pos


def main_app():
    window = Tk()
    app = App(window)
    window.mainloop()


if __name__ == '__main__':
    main_app()
