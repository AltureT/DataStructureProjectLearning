# -*- coding: utf-8 -*-


class User:
    def __init__(self, name='Bob', email='Bob@example.com', tel='123456789'):
        self._name = name
        self._email = email
        self._tel = tel

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def tel(self):
        return self._tel


class LinkNode:
    def __init__(self, val: User):
        self.val = val
        self.next = None


class TreeNode:
    def __init__(self, val: User):
        self.val = val
        self.left = None
        self.right = None
