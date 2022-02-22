# -*- coding: utf-8 -*-
import re

from model import *


def array_find(data: list, name: str) -> User:
    """
    目的：从数组形式存储的用户数据中根据用户姓名查找信息，data数组已经根据姓名做升序排序。
    :param data: 数组方式存储的用户:[User(1),User(2),User(3)....]，获取data[0]用户姓名的方式（str类型）：data[0].get_user_name()
    :param name: 待查找对象的姓名
    :return: 返回用户对象 User,若不存在返回 None
    """
    for i in data:
        if i.get_user_name() == name:
            return i
    return None


def link_find(root: LinkNode, name):
    """
    目的：从链表中根据用户姓名查找用户信息,链表已经根据姓名升序
    节点模型：
    class LinkNode:
        def __init__(self, val: User):
            self.val = val
            self.next = None
    :param root:链表的表头,获取当前节点姓名的方式：root.val.get_user_name()
    :param name:待查找对象的姓名
    :return:返回用户对象 User,若不存在返回 None
    """
    cur = root
    while cur:
        if cur.val.get_user_name() == name:
            return cur.val
        cur = cur.next
    return None


def tree_find(root: TreeNode, name):
    """
    目的：从二叉树中根据用户姓名查找用户信息,树已经根据姓名排序，保证左子树姓名小于右子树
    节点模型：
    class TreeNode:
        def __init__(self, val: User):
            self.val = val
            self.left = None
            self.right = None
    :param root:树的的根节点,获取当前节点姓名的方式：root.val.get_user_name()
    :param name:待查找对象的姓名
    :return:返回用户对象 User,若不存在返回 None
    """

    pass


def array_add(data: list, u: User) -> list:
    data.append(u)
    return data


def link_add(root: LinkNode, u: User):
    pass


def tree_add(root: TreeNode, u: User):
    pass


def check_email(email) -> bool:
    if re.match(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',
                email) is not None:
        return True
    return False


def check_tel(tel) -> bool:
    if len(tel) != 11:
        return False
    elif tel[0] != "1":
        return False
    elif tel[1:2] != "3" and tel[1:2] != "5" and tel[1:2] != "7" and tel[1:2] != "8":
        return False
    for i in range(2, 11):
        if tel[i] < "0" or tel[i] > "9":
            return False
    return True


def log_add(queue: list, operat: str, obj: str):
    pass
