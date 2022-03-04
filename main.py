# -*- coding: utf-8 -*-
import threading
import time
from tkinter import *
from tkinter import ttk

import model

config = {'env': 'dev'}
if config['env'] == 'dev':
    import solution_dev as solution
    import global_val_dev as global_val
else:
    import solution as solution
    import global_val as global_val


class Decorator:
    def __init__(self, text='control'):
        self.text = text

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(kwargs)
            name = kwargs
            s = self.text + name
            solution.log_add(global_val.get_log_queue(), s)

            self.logresult.delete(1.0, 'end')
            for i in global_val.get_log_queue():
                self.logresult.insert(END, i + '\n')

            func(*args, **kwargs)

        return wrapper


class App:
    def __init__(self, window):
        self.sresult = Text()
        self.aresult = Text()
        self.logresult = Text()
        self.windowName = window
        global_val._init()
        self.create_widgets()

    def create_widgets(self):
        self.windowName.title('通讯录')
        self.windowName.geometry('730x430')

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
                               command=lambda: self.from_array(nameentry.get()))
        searchbutton2 = Button(searchtabframe, text='查询（链表）',
                               command=lambda: self.from_link(nameentry.get()))
        searchbutton3 = Button(searchtabframe, text='查询（二叉树）',
                               command=lambda: self.from_tree(nameentry.get()))
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
                            command=lambda: self.add_to_array(
                                nameentry.get(), emailentry.get(), telentry.get()))

        addbutton2 = Button(addtabframe, text='新增（链表）',
                            command=lambda: self.add_to_link(
                                nameentry.get(), emailentry.get(), telentry.get()))

        addbutton3 = Button(addtabframe, text='新增（二叉树）',
                            command=lambda: self.add_to_tree(
                                nameentry.get(), emailentry.get(), telentry.get()))

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

    def report_log(self, opera: str, name: str):
        s = opera + name
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        result = solution.log_add(global_val.get_log_queue(), s)
        result[len(result) - 1] = t + result[len(result) - 1]
        global_val.set_log_queue(result)
        self.logresult.delete(1.0, 'end')
        for i in global_val.get_log_queue():
            self.logresult.insert(END, i + '\n')

    def log_system(self):
        namelabel = Label(self.windowName, text='操作日志')
        namelabel.grid(row=0, column=2)
        self.logresult = Text(self.windowName)
        self.logresult['width'] = 40
        self.logresult['height'] = 30
        self.logresult.grid(row=1, column=2)

    def check_rule(self, email, tel) -> bool:
        if not solution.check_email(email):
            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '邮箱格式不正确，请重新输入')
            return False
        if not solution.check_tel(tel):
            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '手机号格式不正确，请重新输入')
            return False
        return True

    def output(self, st: str, result: model.User) -> None:
        if result:
            s = st + '\n' + \
                result.name + '\n' + \
                result.email + '\n' + \
                result.tel + '\n'
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, s)
        else:
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, '该数据结构中用户不存在')

    def _from_array(self, name):
        if len(name) == 0:
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, '请输入姓名查找')
            return
        result = solution.array_find(global_val.get_user_array(), name)
        self.output('从数组结构中找到：', result)
        self.report_log('从数组中查询：', name)

    def from_array(self, name):
        t = threading.Thread(target=self._from_array(name))
        t.start()

    def _from_link(self, name):
        if len(name) == 0:
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, '请输入姓名查找')
            return

        result = solution.link_find(global_val.get_user_link(), name)
        self.output('从链表结构中找到：', result)
        self.report_log('从链表中查询：', name)

    def from_link(self, name):
        t = threading.Thread(target=self._from_link(name))
        t.start()

    def _from_tree(self, name):
        if len(name) == 0:
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, '请输入姓名查找')
            return

        result = solution.tree_find(global_val.get_user_tree(), name)
        self.output('从树结构中找到：', result)
        self.report_log('从树中查询：', name)

    def from_tree(self, name):
        t = threading.Thread(target=self._from_tree(name))
        t.start()

    def _add_to_array(self, name, email, tel):
        if len(name) == 0:
            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '请输入姓名添加')
            return

        if self.check_rule(email, tel):
            u = model.User(name, email, tel)
            newarray = solution.array_add(global_val.get_user_array(), u)
            global_val.set_user_array(newarray)

            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '新增到数组成功')
            self.report_log('添加该用户到数组：', name)

    def add_to_array(self, name, email, tel):
        t = threading.Thread(target=self._add_to_array(name, email, tel))
        t.start()

    def _add_to_link(self, name, email, tel):
        if len(name) == 0:
            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '请输入姓名添加')
            return

        if self.check_rule(email, tel):
            u = model.User(name, email, tel)
            newlink = solution.link_add(global_val.get_user_link(), model.LinkNode(u))
            global_val.set_user_link(newlink)

            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '新增到链表成功')
            self.report_log('添加该用户到链表：', name)

    def add_to_link(self, name, email, tel):
        t = threading.Thread(target=self._add_to_link(name, email, tel))
        t.start()

    def _add_to_tree(self, name, email, tel):
        if len(name) == 0:
            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '请输入姓名添加')
            return
        if self.check_rule(email, tel):
            u = model.User(name, email, tel)
            newtree = solution.tree_add(global_val.get_user_tree(), model.TreeNode(u))
            global_val.set_user_tree(newtree)

            self.aresult.delete(1.0, 'end')
            self.aresult.insert(1.0, '新增到树成功')
            self.report_log('添加该用户到树：', name)

    def add_to_tree(self, name, email, tel):
        t = threading.Thread(target=self._add_to_tree(name, email, tel))
        t.start()


def main_app():
    window = Tk()
    app = App(window)
    window.mainloop()


if __name__ == '__main__':
    main_app()
