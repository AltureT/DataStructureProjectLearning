# -*- coding: utf-8 -*-
import threading
import time
from collections.abc import Iterable
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import networkx as nx

import fake
import global_val
import model

config = {'env': 'dev'}

plt.rcParams["font.sans-serif"] = ['Arial Unicode MS', 'SimHei']
plt.rcParams["axes.unicode_minus"] = False

if config['env'] == 'dev':
    import solution_dev as solution
else:
    import solution as solution


class BinaryTree:

    def __init__(self, seq=()):
        assert isinstance(seq, Iterable)  # 确保输入的参数为可迭代对象
        self.root = None


class Graph:
    def create_graph(self, G, node, pos=None, x=0, y=0, layer=1):
        if node is None:
            return
        if pos is None:
            pos = {}
        pos[node.val.name] = (x, y)
        if node.left:
            G.add_edge(node.val.name, node.left.val.name)
            l_x, l_y = x - 1 / 2 ** layer, y - 1
            l_layer = layer + 1
            self.create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
        if node.right:
            G.add_edge(node.val.name, node.right.val.name)
            r_x, r_y = x + 1 / 2 ** layer, y - 1
            r_layer = layer + 1
            self.create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
        return (G, pos)

    def _draw(self, node):  # 以某个节点为根画图
        print('绘制图中·······')
        if node is None:
            print('节点不存在·······')
            return
        graph = nx.DiGraph()
        graph, pos = self.create_graph(graph, node)
        # fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
        global_val.set_graph(graph)
        global_val.set_pos(pos)
        # global_val.set_ax(ax)
        # nx.draw_networkx(graph, pos, ax=ax, node_size=300)
        # plt.show()
        # print('绘制完成')

    def draw(self):  # 以某个节点为根画图
        t = threading.Thread(target=lambda: self._draw(global_val.get_user_tree()))
        t.start()


class Control:
    def __init__(self):
        pass

    @staticmethod
    def generate_data(s):
        s = s if len(s) > 0 else '0'
        n = int(s)
        t = threading.Thread(target=lambda: fake.fake_data(n))
        t.start()


class App:
    def __init__(self, window):
        self.sresult = Text()
        self.aresult = Text()
        self.logresult = Text()
        self.windowName = window
        global_val.init()
        self.create_widgets()

    def create_widgets(self):
        self.windowName.title('通讯录')
        self.windowName.geometry('730x460')

        tabs = ttk.Notebook(self.windowName, width=370, height=360)
        searchtabframe = Frame(tabs)
        self.create_search_frame(searchtabframe)

        addtabframe = Frame(tabs)
        self.create_add_frame(addtabframe)

        createtabframe = Frame(tabs)
        self.create_create_frame(createtabframe)

        self.create_log_window()

        tabs.add(searchtabframe, text='查询')
        tabs.add(addtabframe, text='新增')
        tabs.add(createtabframe, text='数据生成')
        tabs.grid(row=0, column=0, rowspan=24, columnspan=2)

        author = '项目地址:https://gitee.com/alture/DataStructureProjectLearning'
        namelabel = Label(self.windowName, text=author)
        namelabel.grid(row=3, column=0, columnspan=2)

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
        searchbutton4 = Button(searchtabframe, text='打印二叉树）',
                               command=self.draw_tree)
        namelabel.grid(row=0, column=0, padx=10, pady=5, ipady=10)
        nameentry.grid(row=0, column=1, padx=10, pady=10, ipady=10)
        searchbutton1.grid(row=1, column=0, padx=10, pady=5, ipady=10)
        searchbutton2.grid(row=2, column=0, padx=10, pady=5, ipady=10)
        searchbutton3.grid(row=3, column=0, padx=10, pady=5, ipady=10)
        searchbutton4.grid(row=4, column=0, padx=10, pady=5, ipady=10)

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

    def create_create_frame(self, createtabframe):
        sizelabel = Label(createtabframe, text='生成数据量:')
        size = StringVar()
        sizeentry = Entry(createtabframe, textvariable=size)
        button1 = Button(createtabframe, text='数据生成',
                         command=lambda: self.create_data(sizeentry.get()))

        button2 = Button(createtabframe, text='数据重置',
                         command=self.initial_data)

        sizelabel.grid(row=0, column=0, padx=10, pady=5, ipady=5)
        sizeentry.grid(row=0, column=1, padx=10, pady=10, ipady=5)
        button1.grid(row=3, column=1, padx=10, pady=5, ipady=10)
        button2.grid(row=4, column=1, padx=10, pady=5, ipady=10)

    def create_log_window(self):
        namelabel = Label(self.windowName, text='操作日志')
        namelabel.grid(row=0, column=2)
        self.logresult = Text(self.windowName)
        self.logresult['width'] = 40
        self.logresult['height'] = 30
        self.logresult.grid(row=1, column=2)

    def draw_tree(self):
        t = threading.Thread(target=Graph().draw())
        t.daemon = True
        t.start()
        # graph = Graph(global_val.get_user_tree())
        # graph.draw()
        # plt.show()
        fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
        graph = global_val.get_graph()
        pos = global_val.get_pos()

        nx.draw_networkx(graph, pos, ax=ax, node_size=300)
        plt.show()
        print('绘制完成')

    def initial_data(self):
        self.logresult.delete(1.0, 'end')
        global_val.init()

    def report_log(self, opera: str, name: str):
        runtime = global_val.get_runtime()
        s = opera + name + '\n' + '时间开销:' + runtime + 'ms'

        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        result = solution.log_add(global_val.get_log_queue(), s)
        result[len(result) - 1] = t + result[len(result) - 1]
        global_val.set_log_queue(result)

        self.logresult.delete(1.0, 'end')

        for i in global_val.get_log_queue():
            self.logresult.insert(END, i + '\n')

    def create_data(self, n):
        t = threading.Thread(target=Control.generate_data(n))
        t.start()

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

    def from_array(self, name):
        if len(name) == 0:
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, '请输入姓名查找')
            return
        result = solution.array_find(global_val.get_user_array(), name)
        self.output('从数组结构中找到：', result)
        self.report_log('从数组中查询：', name)

    def from_link(self, name):
        if len(name) == 0:
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, '请输入姓名查找')
            return
        result = solution.link_find(global_val.get_user_link(), name)
        self.output('从链表结构中找到：', result)
        self.report_log('从链表中查询：', name)

    def from_tree(self, name):
        if len(name) == 0:
            self.sresult.delete(1.0, 'end')
            self.sresult.insert(1.0, '请输入姓名查找')
            return
        result = solution.tree_find(global_val.get_user_tree(), name)
        self.output('从树结构中找到：', result)
        self.report_log('从树中查询：', name)

    def add_to_array(self, name, email, tel):
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

    def add_to_link(self, name, email, tel):
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

    def add_to_tree(self, name, email, tel):
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


def main_app():
    window = Tk()
    app = App(window)
    window.mainloop()


if __name__ == '__main__':
    main_app()
