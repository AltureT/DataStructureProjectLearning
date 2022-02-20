# -*- coding: utf-8 -*-
import global_val
import model
from model import *


def array_find(data: list, name: str) -> model.User:
    '''
    从数组形式存储的学生数据中查找学生信息
    :param data: 数组方式存储的学生:[User(1),User(2),User(3)....]
    :param name: 需要查询的姓名
    :return: 返回用户对象,若不存在返回 None
    格式：return i
    '''
    for i in data:
        if i.get_user_name() == name:
            return i
    return None


def link_find(root: LinkNode, name):
    pass


def tree_find(root: TreeNode, name):
    pass


def array_add(name, email, tel):
    pass


def link_add(name, email, tel):
    pass


def tree_add(name, email, tel):
    pass
