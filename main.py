# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

import model

config = {'env': 'dev'}
if config['env'] == 'dev':
    import solutiondev as solution
    import global_val_dev as global_val
else:
    import solution as solution
    import global_val as global_val


class App:
    def __init__(self, windowName):
        self.sresult = Text()
        self.aresult = Text()
        self.logresult = Text()
        self.windowName = windowName
        global_val.init()
        self.create_widgets()

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
                               command=lambda: self.exec_and_output(0, 0, [nameentry.get()]))
        searchbutton2 = Button(searchtabframe, text='查询（链表）',
                               command=lambda: self.exec_and_output(0, 1, [nameentry.get()]))
        searchbutton3 = Button(searchtabframe, text='查询（二叉树）',
                               command=lambda: self.exec_and_output(0, 2, [nameentry.get()]))
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
                            command=lambda: self.exec_and_output(1, 0,
                                                                 [nameentry.get(), emailentry.get(), telentry.get()]))
        addbutton2 = Button(addtabframe, text='新增（链表）',
                            command=lambda: self.exec_and_output(1, 1,
                                                                 [nameentry.get(), emailentry.get(), telentry.get()]))
        addbutton3 = Button(addtabframe, text='新增（二叉树）',
                            command=lambda: self.exec_and_output(1, 2,
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

    def exec_and_output(self, code1: int, code2: int, info: list):
        """
        执行查找/新增，并做输出处理
        :param code1: 0代表查找，1代表新增
        :param code2: 0代表数组，1代表链表，2代表树
        :param info: [name,email,tel]
        :return:
        """
        result = ''
        self.sresult.delete(1.0, 'end')
        if code1 == 0:
            name = info[0]
            if code2 == 0:
                result = self.from_array(name)
            elif code2 == 1:
                result = self.from_link(name)
            else:
                result = self.from_tree(name)

            if result:
                self.sresult.insert(1.0, result)
            else:
                self.sresult.insert(1.0, '用户不存在')
        else:
            name = info[0]
            email = info[1]
            tel = info[2]
            if code2 == 0:
                self.add_to_array(name, email, tel)
            elif code2 == 1:
                self.add_to_link(name, email, tel)
            else:
                self.add_to_tree(name, email, tel)
        return

    def update_to_global(self, u: model.User):
        """
        将数据更新到全局变量
        :param u: 待新增用户
        :return:
        """
        global_val.set_user_info(u)

    def from_array(self, name) -> str:
        result = solution.array_find(global_val.get_user_array(), name)
        if result:
            s = result.get_user_name() + '\n' + \
                result.get_user_email() + '\n' + \
                result.get_user_tel() + '\n'
            return s
        return ''

    def from_link(self, name) -> str:
        result = solution.link_find(global_val.get_user_array(), name)
        if result:
            s = result.get_user_name() + '\n' + \
                result.get_user_email() + '\n' + \
                result.get_user_tel() + '\n'
            return s
        return ''

    def from_tree(self, name) -> str:
        result = solution.tree_find(global_val.get_user_array(), name)
        if result:
            s = result.get_user_name() + '\n' + \
                result.get_user_email() + '\n' + \
                result.get_user_tel() + '\n'
            return s
        return ''

    def add_to_array(self, name, email, tel):
        u = model.User(name, email, tel)
        self.update_to_global(u)
        return

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
