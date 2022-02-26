# -*- coding: utf-8 -*-
import re

import model


def array_find(data: list, name: str) -> model.User:
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


def link_find(root: model.LinkNode, name) -> model.User:
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


def tree_find(root: model.TreeNode, name):
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
    if root is None:
        return None

    if root.val.get_user_name() == name:
        return root.val
    elif name < root.val.get_user_name():
        return tree_find(root.left, name)
    else:
        return tree_find(root.right, name)


def array_add(data: list, u: model.User) -> list:
    """
    目的：将数据插入到合适的位置，保持以姓名为主要关键字升序
    :param data:用户数据
    :param u:待插入的用户对象
    :return:插入成功返回新的data
    """
    data.append(u)

    i = len(data) - 2
    while i >= 0 and u.get_user_name() < data[i].get_user_name():
        data[i + 1] = data[i]
        i -= 1
    data[i + 1] = u

    return data


def output_link(root):
    while root:
        print(root.val.get_user_name())
        root = root.next


def link_add(root: model.LinkNode, u: model.LinkNode):
    head = root
    cur = head
    if cur is None:
        head = u
        return head

    if cur.val.get_user_name() > u.val.get_user_name():
        u.next = cur
        head = u
        return head

    while cur:
        if cur.next is None:
            cur.next = u
            return head
        if cur.next.val.get_user_name() > u.val.get_user_name():
            u.next = cur.next
            cur.next = u
            return head
        cur = cur.next


def tree_add(root: model.TreeNode, u: model.TreeNode):
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
