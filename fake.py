# -*- coding: utf-8 -*-

from faker import Faker

import global_val
from model import *
from solution_dev import *


def fake_data(n):
    fakecn = Faker(locale='zh_CN')
    fakeus = Faker(locale='en_US')
    dic = {}
    i = 0
    c = n if n <= 10000 else 10000
    while i < c:
        name = fakeus.name()
        email = fakeus.email()
        tel = fakecn.phone_number()

        if name not in dic:
            i += 1
            dic[name] = None

            u = User(name, email, tel)
            nlink = LinkNode(u)
            ntree = TreeNode(u)
            r1 = array_add(global_val.get_user_array(), u)
            global_val.set_user_array(r1)
            r2 = link_add(global_val.get_user_link(), nlink)
            global_val.set_user_link(r2)
            r3 = tree_add(global_val.get_user_tree(), ntree)
            global_val.set_user_tree(r3)
            print('第', i, '条', name, email, tel)
    if n > 10000:
        print('由于性能原因，一次性最多生成10000条数据')
    print('数据生成完成')
