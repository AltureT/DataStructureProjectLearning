# -*- coding: utf-8 -*-


class User():
    def __init__(self, name, email, tel):
        self._name = name
        self._email = email
        self._tel = tel

    def get_user_name(self):
        return self._name

    def get_user_email(self):
        return self._email

    def get_user_tel(self):
        return self._tel


class LinkNode():
    def __init__(self, val: User):
        self.val = val
        self.next = None


class TreeNode():
    def __init__(self, val: User):
        self.val = val
        self.left = None
        self.right = None
