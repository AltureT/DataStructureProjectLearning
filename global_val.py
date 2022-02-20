# -*- coding: utf-8 -*-
import model


def _init():
    global _global_user_array
    global _global_user_link
    global _global_user_tree
    global _global_log_queue
    global _global_user_obj

    testuser = model.User(name='Bob', email='Bob@example.com', tel='123456789')

    _global_user_obj = testuser
    _global_user_array = [testuser]
    _global_user_link = model.LinkNode(testuser)
    _global_user_tree = model.TreeNode(testuser)

    _global_log_queue = []


def init():
    _init()


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


def set_user_array(array):
    try:
        _global_user_array = array
    except NameError as e:
        print(e, 'global未初始化')


def set_user_link(link):
    try:
        _global_user_link = link
    except NameError as e:
        print(e, 'global未初始化')


def set_user_tree(tree):
    try:
        _global_user_tree = tree
    except NameError as e:
        print(e, 'global未初始化')


def set_log_queue(list):
    try:
        _global_log_queue = list
    except NameError as e:
        print(e, 'global未初始化')
