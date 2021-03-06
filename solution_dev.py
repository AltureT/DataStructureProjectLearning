# -*- coding: utf-8 -*-
import re

import model
from decorator import runtime


@runtime
def array_find(data: list, name: str) -> model.User:
    """
    目的：从data中寻找name的信息，data数组已经根据姓名做升序排序。
    :param data: 数组方式存储的用户:如[User('Alice'),User('Bob'),User('Tom')....]，
        获取data[0]用户姓名的方式（str类型）：data[0].name
    :param name: 待查找对象的姓名（str类型）
    :return: 返回找到的用户对象 User,若不存在返回 None
    """
    i, j = 0, len(data) - 1
    while i <= j:
        m = (i + j) // 2
        if data[m].name == name:
            return data[m]
        elif data[m].name > name:
            j = m - 1
        else:
            i = m + 1
    return None


@runtime
def link_find(root: model.LinkNode, name: str) -> model.User:
    """
    目的：从root链表中查找name用户信息,链表已经根据姓名升序
    节点模型：
    class LinkNode:
        def __init__(self, val: User):
            self.val = val
            self.next = None
    用户模型：
    class User:
        def __init__(self, name:str, email:str, tel:str):
            self._name = name
            self._email = email
            self._tel = tel
    :param root:链表的表头（LinkNode类型）,获取当前节点姓名的方式：root.val.name
    :param name:待查找对象的姓名（str类型）
    :return:返回找到的用户对象 User,若不存在返回 None
    """
    cur = root
    while cur:
        if cur.val.name == name:
            return cur.val
        cur = cur.next
    return None


@runtime
def tree_find(root: model.TreeNode, name: str):
    """
    目的：从二叉树中根据用户姓名查找用户信息,树已经根据姓名排序，保证左子树姓名小于右子树
    节点模型：
    class TreeNode:
        def __init__(self, val: User):
            self.val = val
            self.left = None
            self.right = None
    用户模型：
    class User:
        def __init__(self, name:str, email:str, tel:str):
            self._name = name
            self._email = email
            self._tel = tel
    :param root:树的的根节点(LinkNode类型),获取当前节点姓名的方式：root.val.name
    :param name:待查找对象的姓名（str类型）
    :return:返回找到的用户对象 User,若不存在返回 None
    """
    if root is None:
        return None

    if root.val.name == name:
        return root.val
    elif name < root.val.name:
        return tree_find(root.left, name)
    else:
        return tree_find(root.right, name)


@runtime
def array_add(data: list, u: model.User) -> list:
    """
    目的：将用户数据u插入到合适的位置，保持以姓名为主要关键字升序
    :param data:用户数据，data列表中的元素是User类，可以通过如：data[0].get_user_name获取用户姓名
    :param u:待插入的用户对象
    :return:返回插入后的新data
    """
    data.append(u)

    i = len(data) - 2
    while i >= 0 and u.name < data[i].name:
        data[i + 1] = data[i]
        i -= 1
    data[i + 1] = u

    return data


@runtime
def link_add(root: model.LinkNode, u: model.LinkNode) -> model.LinkNode:
    """
    目的：将u节点插入到链表合适的位置，保持以姓名为主要关键字升序
    节点模型：
    class LinkNode:
        def __init__(self, val: User):
            self.val = val
            self.next = None
    用户模型：
    class User:
        def __init__(self, name:str, email:str, tel:str):
            self._name = name
            self._email = email
            self._tel = tel
    :param root:用户数据链表表头,获取当前节点用户姓名的方式：root.val.name
    :param u:等待插入的用户节点,获取节点 u 姓名的方式：u.val.name
    :return:返回新的链表表头节点
    """
    head = root
    cur = head
    if cur is None:
        head = u
        return head

    if cur.val.name > u.val.name:
        u.next = cur
        head = u
        return head

    while cur:
        if cur.next is None:
            cur.next = u
            return head
        if cur.next.val.name > u.val.name:
            u.next = cur.next
            cur.next = u
            return head
        cur = cur.next


@runtime
def tree_add(root: model.TreeNode, u: model.TreeNode) -> model.TreeNode:
    """
    目的：将新用户u，添加到二叉树中合适位置，保证左子树小于右子树
    节点模型：
    class TreeNode:
        def __init__(self, val: User):
            self.val = val
            self.left = None
            self.right = None
    用户模型：
    class User:
        def __init__(self, name:str, email:str, tel:str):
            self._name = name
            self._email = email
            self._tel = tel
    :param root: 存储用户数据的树结构的根结点,获取当前节点用户姓名的方式：root.val.name
    :param u:待新增用户,获取节点 u 姓名的方式：u.val.name
    :return:返回新的树结构的根结点
    """
    cur = root
    if root is None:
        return u

    if u.val.name < cur.val.name:
        if cur.left:
            cur.left = tree_add(cur.left, u)
        else:
            cur.left = u
    else:
        if cur.right:
            cur.right = tree_add(cur.right, u)
        else:
            cur.right = u
    return cur


@runtime
def check_email(email: str) -> bool:
    """
    目的：检验邮箱合法性，邮箱一般包含 @ 符号与顶级域名
    :param email: 待检验邮箱
    :return: 邮箱合法返回True，否则返回False
    """
    if re.match(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',
                email) is not None:
        return True
    return False


@runtime
def check_tel(tel: str) -> bool:
    """
    目的：检验手机号合法性，手机号一般1开头，第二位数字一般为3、5、7、8，其余位是数字
    :param tel: 待检验手机号
    :return: 手机号合法返回True，否则返回False
    """
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


@runtime
def log_add(queue: list, s: str) -> list:
    """
    目的：将新的日志信息 s 更新到 日志队列 queue 中去。按时间顺序升序，保证日志条目最多不超过十条。
    :param queue: 日志队列
    :param s: 新的操作日志内容
    :return: 返回新的队列
    """
    queue.append(s)
    if len(queue) > 10:
        queue = queue[1:11]
    return queue
