# -*- coding: utf-8 -*-
import model

_global_user_array = []
_global_user_link = model.LinkNode(None)
_global_user_tree = model.TreeNode(None)
_global_log_queue = []


def _init():
    global _global_user_array
    global _global_user_link
    global _global_user_tree
    global _global_log_queue
    global _global_user_obj
    testuser = model.User(name='Bob', email='Bob@example.com', tel='123456789')
    testuser2 = model.User(name='Bob2', email='Bob2@example.com', tel='123456789')
    node1 = model.LinkNode(testuser)
    node2 = model.LinkNode(testuser2)
    node1.next = node2

    _global_user_obj = testuser
    _global_user_array = [testuser, testuser2]
    _global_user_link = node1
    _global_user_tree = model.TreeNode(testuser)
    _global_log_queue = []


def get_user_info():
    try:
        return _global_user_obj
    except NameError as e:
        print(e, 'global未初始化')


def get_user_array():
    try:
        return _global_user_array
    except NameError as e:
        print(e, 'global未初始化')


def get_user_link():
    try:
        return _global_user_link
    except NameError as e:
        print(e, 'global未初始化')


def get_user_tree():
    try:
        return _global_user_tree
    except NameError as e:
        print(e, 'global未初始化')


def get_log_queue():
    try:
        return _global_log_queue
    except NameError as e:
        print(e, 'global未初始化')


def set_user_info(obj):
    try:
        _global_user_obj = obj
    except NameError as e:
        print(e, 'global未初始化')


def set_user_array(array: list):
    global _global_user_array
    try:
        _global_user_array = array
    except NameError as e:
        print(e, 'global未初始化')


def set_user_link(root: model.LinkNode):
    global _global_user_link
    try:
        _global_user_link = root
    except NameError as e:
        print(e, 'global未初始化')


def set_user_tree(root: model.TreeNode):
    global _global_user_tree
    try:
        _global_user_tree = root
    except NameError as e:
        print(e, 'global未初始化')


def set_log_queue(list):
    global _global_log_queue
    try:
        _global_log_queue = list
    except NameError as e:
        print(e, 'global未初始化')
